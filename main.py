from flask import Flask, render_template, redirect, url_for, flash, request
from fetch_rss import news_feed_html, get_search_results, get_single_news
import pymysql #nusret
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import logging

class StructuredFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            'IP': request.remote_addr,
            'Page': request.path,
            'Log': record.msg,
            'Date': self.formatTime(record, self.datefmt),
        }
        return str(log_data)

logging.basicConfig(level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                    handlers=[
                        logging.FileHandler('app.log'),  # Log to a file
                        logging.StreamHandler(),         # Log to the console
                    ])

# Set the custom formatter for all handlers
for handler in logging.root.handlers:
    handler.setFormatter(StructuredFormatter())


app = Flask("cs437-project")

app.config['SECRET_KEY'] = 'bro_cs437_is_cool'  # Change this to a random secret key
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:CS437.isthebest@localhost/turkishdb"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '' # nusret
app.config['MYSQL_PASSWORD'] = 'CS437.isthebest'
app.config['MYSQL_DB'] = 'turkishdb'

#db = SQLAlchemy(app)
#mysql = MySQLdb.connect(host = app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                        #password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])

mysql = pymysql.connect(host = app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])  # nusret

cursor = mysql.cursor()

class User(UserMixin):
    def __init__(self, id, username, password, role='user'):
        self.id = id
        self.username = username
        self.password = password
        self.role = role  # Add a role attribute

    def is_admin(self):
        return self.role == 'admin'
    
    def get_comments(self):
        query = 'SELECT * FROM comments WHERE username = %s'
        cursor.execute(query, (self.username,))
        comment_data = cursor.fetchall()

        comments = [Comment(*row) for row in comment_data]
        return comments
    
class Comment:
    def __init__(self, id, username, content, created_at, news_link):
        self.id = id
        self.username = username
        self.content = content
        self.created_at = created_at
        self.news_link = news_link



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

def get_all_comments():
    query = 'SELECT * FROM comments'
    cursor.execute(query)
    comments = cursor.fetchall()

    return comments

# Function to delete a user by user ID
def delete_user_by_id(user_id):

    query = 'DELETE FROM users WHERE id = %s'
    cursor.execute(query, (user_id,))

    mysql.commit()

# Function to delete a user by user ID
def delete_comment_by_id(comment_id):

    query = 'DELETE FROM comments WHERE id = %s'
    cursor.execute(query, (comment_id,))

    mysql.commit()


@app.route("/")
def main_page():
    main_html_content, secondary_html_content, remaining_html_content = news_feed_html()

    # Fetch comments for the current user
    user_comments = current_user.get_comments() if current_user.is_authenticated else []

    if current_user.is_authenticated:
        return render_template('index.html', main_html_content=main_html_content, secondary_html_content=secondary_html_content,
                               remaining_html_content=remaining_html_content, username=current_user.username, comments=user_comments)
    else:
        return render_template('index.html', main_html_content=main_html_content, secondary_html_content=secondary_html_content,
                               remaining_html_content=remaining_html_content, username='guest', comments=user_comments)

@app.route('/search-result', methods=['GET'])
def search_result_page():
    keyword = request.args.get('keyword', '')
    results_html_content = get_search_results(keyword)
    
    if current_user.is_authenticated:
        return render_template('search-result.html', username=current_user.username, results_html_content=results_html_content)
    else:
        return render_template('search-result.html', username='guest', results_html_content=results_html_content)

        
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
        
        app.logger.info("User try to reach forbidden page.")

        return render_template('access_denied.html')

    users = get_all_users() 
    comments = get_all_comments() 
    return render_template('admin.html',users = users, comments = comments, username=current_user.username)


@app.route('/admin/addUser', methods = ['POST'])
@login_required
def admin_add():
    if not current_user.is_admin():

        app.logger.info("User try to reach forbidden page.")
        return render_template('access_denied.html')
    
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        if not username or not password:
            flash('Both username and password are required!', 'error')    
            return

        if(get_user_by_username(username) != None):

            flash("Username is already in use!", 'error')

            return

        hashed_password = generate_password_hash(password, method='pbkdf2:md5')

        cursor.execute('INSERT INTO users (username, password,role) VALUES (%s, %s,%s)', (username, hashed_password, role))
        mysql.commit()
        flash('User registered successfully!', 'success')

    return redirect(url_for('admin'))


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

@app.route("/coins", methods=['POST', 'GET'])
def coins_page():
    if request.method == "POST":
        search_query = request.form.get('search_query')
        the_query = f"SELECT url FROM coins WHERE name = '{search_query}'"

        app.logger.info(f"Query executed: {the_query}")
        cursor.execute(the_query)
        search_results = cursor.fetchall()

        if search_results:
            return redirect(search_results[0][0])
        else:
            return "Coin not found"

    cursor.execute("SELECT id, name FROM coins")
    all_coins = cursor.fetchall()

    if current_user.is_authenticated:
        return render_template('coins.html',username=current_user.username, all_coins=all_coins)
    else:
        return render_template('coins.html',username='guest',  all_coins=all_coins)
    


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
        app.logger.info("User try to reach forbidden page.")
        return render_template('access_denied.html')
    
    delete_user_by_id(user_id)
    return redirect(url_for('admin'))

@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    if not current_user.is_admin():
        app.logger.info("User try to reach forbidden page.")
        return render_template('access_denied.html')
    
    delete_comment_by_id(comment_id)
    return redirect(url_for('admin'))


@app.route('/add_comment', methods=['POST'])
@login_required
def add_comment():
    if request.method == 'POST':
        current_route = request.form.get('current_route')
        message = request.form.get('message')
        news_link = request.form.get('news_link')

        if not message:
            flash('Comment content is required!', 'error')
            return redirect(current_route)

        # Process and store the comment data in the database, including the news link
        query = 'INSERT INTO comments (username, content, news_link) VALUES (%s, %s, %s)'
        cursor.execute(query, (current_user.username, message, news_link))
        mysql.commit()

        flash('Comment submitted successfully!', 'success')

        # Redirect back to the original news article page
        return redirect(request.referrer)

@app.route("/single.html/<keyword>")
def single_news_page(keyword,news_link="/single.html"):
    # Fetch comments related to the current news link
    query = 'SELECT * FROM comments WHERE news_link = %s'
    cursor.execute(query, (news_link,))
    comment_data = cursor.fetchall()
    news = get_single_news(keyword)
    print(news)
    subject = 'Ekonomi'
    title = news.title
    length = len(title)
    image_src = news.links[0]['href']
    source_url = news.link
    redirected_url = "http://127.0.0.1:5000/redirect?url=" + source_url
    description = news.description[length+1:]
    content = news.content[0]['value']
    date = news.published
    news.links[0]['href']
    # Create Comment objects from the retrieved data
    comments = [Comment(*row) for row in comment_data]

    # Pass the current link to the template
    current_news_link = request.path

    
    if current_user.is_authenticated:
        return render_template('single.html', 
                               username=current_user.username, 
                               comments=comments, 
                               current_news_link=current_news_link,
                               title=title,
                               subject=subject,
                               image_src=image_src,
                               description=description,
                               content=content,
                               date=date,
                               redirected_url=redirected_url
                            )
    else:
        return render_template('single.html', 
                            username='guest',
                            comments=comments, 
                            current_news_link=current_news_link,
                            title=title,
                            subject=subject,
                            image_src=image_src,
                            description=description,
                            content=content,
                            date=date,
                            redirected_url=redirected_url
                        )
    


@app.route("/redirect")
def redirect_page():
    if current_user.is_authenticated:
        return render_template('redirect.html', username=current_user.username)
    else:
        return render_template('redirect.html', username='guest')


if __name__ == '__main__':
    app.run(debug=True)


    