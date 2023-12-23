from flask import Flask, render_template, redirect, url_for, flash, request
from fetch_rss import news_feed_html, get_search_results
import MySQLdb
import pymysql #nusret
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask("cs437-project")

app.config['SECRET_KEY'] = 'bro_cs437_is_cool'  # Change this to a random secret key
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:CS437.isthebest@localhost/turkishdb"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' # nusret
app.config['MYSQL_PASSWORD'] = 'CS437.isthebest'
app.config['MYSQL_DB'] = 'turkishdb'

#db = SQLAlchemy(app)
mysql = MySQLdb.connect(host = app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                        password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])

#mysql = pymysql.connect(host = app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])  # nusret

cursor = mysql.cursor()

class User(UserMixin):
    def __init__(self, id, username, password, role='user'):
        self.id = id
        self.username = username
        self.password = password
        self.role = role  # Add a role attribute

    def is_admin(self):
        return self.role == 'admin'
    
    def comments(self):
        query = 'SELECT * FROM COMMENTS WHERE user_id = %s'
        cursor.execute(query, (self.id,))
        return cursor.fetchall()
    
class Comment:
    def __init__(self, id, user_id, content, created_at):
        self.id = id
        self.user_id = user_id
        self.content = content
        self.created_at = created_at

@login_manager.user_loader
def load_user(user_id):
    user_data = get_user_by_id(user_id)
    return User(user_data[0], user_data[1], user_data[2], role=user_data[3])

def get_user_by_username(username):
    try:
        query = 'SELECT * FROM users WHERE username = %s'
        cursor.execute(query, (username,))
        
        # Log the query for debugging
        print(f"Executing query: {query}, Parameters: {username}")
        
        user_data = cursor.fetchone()
        return user_data
    except Exception as e:
        print(f"Error in get_user_by_username: {e}")
        return None


def get_user_by_id(user_id):
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user_data = cursor.fetchone()
    return user_data


def get_all_users():
    query = 'SELECT * FROM users'
    cursor.execute(query)
    users = cursor.fetchall()

    return users

# Function to delete a user by user ID
def delete_user_by_id(user_id):

    query = 'DELETE FROM users WHERE id = %s'
    cursor.execute(query, (user_id,))

    mysql.commit()


@app.route("/")
def main_page():
    main_html_content, secondary_html_content, remaining_html_content = news_feed_html()

    #Fetch comments for the current user
    user_comments = current_user.comments() if current_user.is_authenticated else []

    if current_user.is_authenticated:
        return render_template('index.html',main_html_content=main_html_content,secondary_html_content=secondary_html_content, remaining_html_content= remaining_html_content, username=current_user.username, comment=user_comments)
    else:
        return render_template('index.html',main_html_content=main_html_content, secondary_html_content=secondary_html_content, remaining_html_content= remaining_html_content,username='guest', comments=user_comments)


@app.route('/search-result/<keyword>', methods=['GET'])
def search_result_page(keyword):
    results_html_content = get_search_results(keyword)
    if current_user.is_authenticated:
        return render_template('search-result.html', username=current_user.username, keyword=keyword, results_html_content=results_html_content)
    else:
        return render_template('search-result.html', username='guest', keyword=keyword, results_html_content=results_html_content)

        
@app.route("/login.html", methods = ['POST', 'GET'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_data = get_user_by_username(username)

        if user_data and check_password_hash(user_data[2], password):
            user = User(user_data[0], user_data[1], user_data[2],user_data[3])
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main_page'))
        else:
            flash('Invalid username or password', 'error')
    
    if current_user.is_authenticated:
        return render_template('login.html',username=current_user.username)
    else:
        return render_template('login.html',username='guest')

@app.route("/sign-up.html", methods = ['POST', 'GET'])
def sign_up_page():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        check =  request.form.get('check_password')
        if not username or not password:
            flash('Both username and password are required!', 'error')
            return redirect(url_for('sign_up_page'))
        
        if(password != check):
            flash("Passwords do not match!", 'error')

            return redirect(url_for('sign_up_page'))
        if(get_user_by_username(username) != None):

            flash("Username is already in use!", 'error')

            return redirect(url_for('sign_up_page'))

        hashed_password = generate_password_hash(password, method='pbkdf2:md5')

        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        mysql.commit()
        flash('User registered successfully!', 'success')


        return redirect(url_for('login_page'))
        
    if current_user.is_authenticated:
        return render_template('sign-up.html',username=current_user.username)
    else:
        return render_template('sign-up.html',username='guest')

@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin():
        # Redirect to a different page or show an error message
        return render_template('access_denied.html')

    users = get_all_users() 
    print(users)
    return render_template('admin.html',users = users)

@app.route("/category.html")
def category_page():
    if current_user.is_authenticated:
        return render_template('category.html',username=current_user.username)
    else:
        return render_template('category.html',username='guest')

@app.route("/contact.html")
def contact_page():
    if current_user.is_authenticated:
        return render_template('contact.html',username=current_user.username)
    else:
        return render_template('contact.html',username='guest')

@app.route("/single.html")
def single_news_page():
    if current_user.is_authenticated:
        return render_template('single.html',username=current_user.username)
    else:
        return render_template('single.html',username='guest')
    

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('main_page'))


@app.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    if not current_user.is_admin():
        return render_template('access_denied.html')
    
    delete_user_by_id(user_id)
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/submit_comment', methods=['POST'])
@login_required
def submit_comment():
    comment_content = request.form.get('comment')

    if comment_content:
        query = 'INSERT INTO comments (user_id, content) VALUES (%s, %s)'
        cursor.execute(query, (current_user.id, comment_content))
        mysql.commit()
        flash('Comment submitted successfully!', 'success')
    else:
        flash('Comment cannot be empty!', 'error')
    
    return redirect(url_for('main_page'))

    