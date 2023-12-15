from flask import Flask, render_template, redirect, url_for, flash, request
from fetch_rss import news_feed_html
import MySQLdb
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask("cs437-project")

app.config['SECRET_KEY'] = 'bro_cs437_is_cool'  # Change this to a random secret key
login_manager = LoginManager(app)
login_manager.login_view = 'login'

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:CS437.isthebest@localhost/turkishdb"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'CS437.isthebest'
app.config['MYSQL_DB'] = 'turkishdb'

#db = SQLAlchemy(app)
mysql = MySQLdb.connect(host = app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                        password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])

cursor = mysql.cursor()

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    user_data = get_user_by_id(user_id)
    return User(user_data[0], user_data[1], user_data[2])

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


@app.route("/")
def main_page():
    news_html_content = news_feed_html()
    if current_user.is_authenticated:
        return render_template('index.html',news_html_content=news_html_content,username=current_user.username)
    else:
        return render_template('index.html',news_html_content=news_html_content,username='guest')
    

@app.route("/login.html", methods = ['POST', 'GET'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user_data = get_user_by_username(username)

        if user_data and check_password_hash(user_data[2], password):
            user = User(user_data[0], user_data[1], user_data[2])
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main_page'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

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
        
        hashed_password = generate_password_hash(password, method='pbkdf2:md5')

        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        mysql.commit()
        flash('User registered successfully!', 'success')


        return redirect(url_for('login_page'))
        
    return render_template('sign-up.html')

@app.route("/category.html")
def category_page():
    return render_template('category.html')

@app.route("/contact.html")
def contact_page():
    return render_template('contact.html')

@app.route("/single.html")
def single_news_page():
    return render_template('single.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run(debug=True)