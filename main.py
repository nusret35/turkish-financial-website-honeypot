# Import necessary modules and libraries
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from fetch_rss import news_feed_html, get_search_results, get_single_news  #custom functions for handling RSS feeds
import mysql.connector
from datetime import datetime 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import string
import random

# Define a custom formatter for structured logging, for better readability and management of logs
class StructuredFormatter(logging.Formatter):
    def format(self, record):
        # Create a structured log data dictionary with necessary information
        log_data = {
            'IP': request.remote_addr,  # IP address of the requester
            'Page': request.path,       # Page (route) being accessed
            'Log': record.msg,          # Log message
            'Date': self.formatTime(record, self.datefmt),  # Timestamp of the log
        }
        return str(log_data)

# Configure logging with custom formatter and file/console handlers
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    handlers=[
        logging.FileHandler('app.log'),  # Log to a file named app.log
        logging.StreamHandler(),         # Also log to the console
    ])

# Set the custom formatter for all handlers to use our StructuredFormatter
for handler in logging.root.handlers:
    handler.setFormatter(StructuredFormatter())

# Create a Flask application with a custom name
app = Flask("cs437-project")

# Set a secret key for session management (change this to a random secret key for production)
app.config['SECRET_KEY'] = 'bro_cs437_is_cool'

# Initialize Flask-Login for user authentication management
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

# Configure database connection parameters for MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'CS437.isthebest'  # Set your MySQL password here
app.config['MYSQL_DB'] = 'turkishdb'

# Create a MySQL database connection
mysql = mysql.connector.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                        password=app.config['MYSQL_PASSWORD'], database=app.config['MYSQL_DB'])
cursor = mysql.cursor(buffered=True)

# Define a User class for Flask-Login with UserMixin for implementing user authentication methods
class User(UserMixin):
    def __init__(self, id, username, password, role='user'):
        self.id = id
        self.username = username
        self.password = password
        self.role = role  # Role attribute to differentiate between admin and normal users

    def is_admin(self):
        # Method to check if the user is an admin
        return self.role == 'admin'

    def get_comments(self):
        # Method to get comments made by the user from the database
        query = 'SELECT * FROM comments WHERE username = %s'
        cursor.execute(query, (self.username,))
        comment_data = cursor.fetchall()
        comments = [Comment(*row) for row in comment_data]
        return comments

# Define a Comment class to represent comments in the system
class Comment:
    def __init__(self, id, username, content, created_at, news_link):
        self.id = id
        self.username = username
        self.content = content
        self.created_at = created_at  # Time when the comment was created
        self.news_link = news_link  # Associated news link of the comment

# Define a user_loader function for Flask-Login to load a user by their user ID
        
@login_manager.user_loader
def load_user(user_id):
    user_data = get_user_by_id(user_id)
    # Return a User object constructed from the user data
    return User(user_data[0], user_data[1], user_data[2], role=user_data[3])

# Function to retrieve user data by username from the database
def get_user_by_username(username):
    try:
        query = 'SELECT * FROM users WHERE username = %s'
        cursor.execute(query, (username,))
        user_data = cursor.fetchone()
        return user_data
    except Exception as e:
        print(f"Error in get_user_by_username: {e}")
        return None

# Function to retrieve user data by user ID from the database
def get_user_by_id(user_id):
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user_data = cursor.fetchone()
    return user_data

# Function to retrieve all users from the database
def get_all_users():
    query = 'SELECT * FROM users'
    cursor.execute(query)
    users = cursor.fetchall()
    return users

# Function to retrieve all comments from the database
def get_all_comments():
    query = 'SELECT * FROM comments'
    cursor.execute(query)
    comments = cursor.fetchall()
    return comments

# Function to delete a user by their user ID
def delete_user_by_id(user_id):
    query = 'DELETE FROM users WHERE id = %s'
    cursor.execute(query, (user_id,))
    mysql.commit()  # Commit the changes to the database

# Function to delete a comment by its comment ID
def delete_comment_by_id(comment_id):
    query = 'DELETE FROM comments WHERE id = %s'
    cursor.execute(query, (comment_id,))
    mysql.commit()  # Commit the changes to the database


def generate_random_username():
    return ''.join(random.choices(string.ascii_lowercase, k=8))

def is_username_unique(username):
    with mysql.cursor() as cursor:
        sql = "SELECT COUNT(*) as count FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
        return result[0] == 0

@app.route('/generate_100_users')
def generate_100_users():
    if not current_user.is_admin():
        app.logger.info("User try to reach forbidden page.")
        return render_template('access_denied.html')
    try:
        hashed_password = generate_password_hash("123456", method='pbkdf2:md5')

        with mysql.cursor() as cursor:
            for _ in range(25):
                username = generate_random_username()
                while not is_username_unique(username):
                    username = generate_random_username()

                password = hashed_password
                role = 'user'

                # Adjust the SQL query based on your table structure
                sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"
                cursor.execute(sql, (username, password, role))

        mysql.commit()
        return redirect(url_for("admin"))
        
    except Exception as e:
        return f"Error: {str(e)}"


# Define a route for recording ad clicks
@app.route('/record_ad_click', methods=['POST'])
def record_ad_click():
    # Record ad clicks by inserting a record into the TRACKAD table with the current user or 'guest'
    # and the URL of the ad
    if current_user.is_authenticated:
        # Insert record for authenticated user
        cursor.execute("INSERT INTO TRACKAD (user, date, url) VALUES (%s, NOW(), %s)", (current_user.username, 'https://www.eye-tech.co.uk'))
    else:
        # Insert record for guest
        cursor.execute("INSERT INTO TRACKAD (user, date, url) VALUES (%s, NOW(), %s)", ('Misafir', 'https://www.eye-tech.co.uk'))

    # Commit changes to the database
    mysql.commit()
    # Return a success response as JSON
    return jsonify({"success": True})

# Define the main page route
@app.route("/")
def main_page():
    # Fetch the news feed content from an external function or service
    main_html_content, secondary_html_content, remaining_html_content = news_feed_html()

    # Fetch comments for the current user if authenticated; otherwise, use an empty list
    user_comments = current_user.get_comments() if current_user.is_authenticated else []

    # Render the main page template with fetched news content and comments
    # Customize the username based on authentication status
    if current_user.is_authenticated:
        return render_template('index.html', main_html_content=main_html_content, secondary_html_content=secondary_html_content,
                               remaining_html_content=remaining_html_content, username=current_user.username, comments=user_comments)
    else:
        return render_template('index.html', main_html_content=main_html_content, secondary_html_content=secondary_html_content,
                               remaining_html_content=remaining_html_content, username='Misafir', comments=user_comments)

# Define a route for search results
@app.route('/search-result/', methods=['GET'])
def search_result_page():
    # Retrieve the keyword from the query parameters and sanitize against XSS
    keyword = request.args.get('keyword', '')

    if "<" in keyword or ">" in keyword:
        app.logger.info(f"Reflected XSS attack on Search Keyword: {keyword}")

    # Fetch the search results based on the keyword (VULNERABILITY)
    results_html_content = get_search_results(keyword)

    # Render the search results page template, customizing the username based on authentication status
    if current_user.is_authenticated:
        return render_template('search-result.html', username=current_user.username, results_html_content=results_html_content)
    else:
        return render_template('search-result.html', username='Misafir', results_html_content=results_html_content)

# Define the login page route
@app.route("/login.html", methods=['POST', 'GET'])
def login_page():
    # Redirect authenticated users to the main page
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))

    # Handle the POST request from the login form
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if ";" in username or ";" in username:
            app.logger.info(f"SQL Injection attack tried by username: {username} and password: {password}")
        
        # Fetch user data from the database based on the provided username
        user_data = get_user_by_username(username)

        # Verify the provided password and log in the user if it's correct
        if user_data and check_password_hash(user_data[2], password):
            user = User(user_data[0], user_data[1], user_data[2], user_data[3])
            login_user(user)
            if(user_data[3] == "admin"):
                return redirect(url_for('admin'))
            flash('Giriş Başarılı!', 'success')  # Show success message
            return redirect(url_for('main_page'))
        else:
            flash('Geçersiz kullanıcı adı veya şifre', 'error')  # Show error message

    # Render the login page template, customizing the username based on authentication status
    if current_user.is_authenticated:
        return render_template('login.html', username=current_user.username)
    else:
        return render_template('login.html', username='Misafir')

# Define the sign-up page route
@app.route("/sign-up.html", methods=['POST', 'GET'])
def sign_up_page():
    # Handle the POST request from the sign-up form
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        check = request.form.get('check_password')
        if ";" in username or ";" in username or ";" in check:
            app.logger.info(f"SQL Injection attack tried by username: {username}, password: {password} check: {check}")

        # Validate that both username and password are provided
        if not username or not password:
            flash('Kullanıcı adınızı ve şifrenizi girdiğinizden emin olun!', 'error')
            return redirect(url_for('sign_up_page'))
        
        # Ensure the provided passwords match
        if(password != check):
            flash("Şifreler eşleşmiyor!", 'error')
            return redirect(url_for('sign_up_page'))
        
        # Check if the username already exists in the database
        if(get_user_by_username(username) != None):
            flash("Kullanıcı adı önceden alınmış!", 'error')
            return redirect(url_for('sign_up_page'))

        # Hash the provided password and insert the new user into the database
        hashed_password = generate_password_hash(password, method='pbkdf2:md5')
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        mysql.commit()
        flash('Üye Oldunuz!', 'success')  # Show success message

        # Redirect to the login page after successful sign-up
        return redirect(url_for('login_page'))
        
    # Render the sign-up page template, customizing the username based on authentication status
    if current_user.is_authenticated:
        return render_template('sign-up.html', username=current_user.username)
    else:
        return render_template('sign-up.html', username='Misafir')

# Define the admin page route
@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin():
        app.logger.info("User try to reach forbidden page.")
        return render_template('access_denied.html')

    users = get_all_users() 
    comments = get_all_comments() 
    return render_template('admin.html', users=users, comments=comments, username=current_user.username)

# Define a route to add a user by an admin
@app.route('/admin/addUser', methods=['POST'])
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
            flash('Kullanıcı adınızı ve şifrenizi girdiğinizden emin olun!', 'error')    
            return

        if(get_user_by_username(username) != None):
            flash("Kullanıcı adı önceden alınmış!", 'error')
            return

        hashed_password = generate_password_hash(password, method='pbkdf2:md5')

        cursor.execute('INSERT INTO users (username, password,role) VALUES (%s, %s,%s)', (username, hashed_password, role))
        mysql.commit()
        flash('Üye Oldunuz!', 'success')

    return redirect(url_for('admin'))


# Define the route for the coins page which allows users to search for coins
@app.route("/coins", methods=['POST', 'GET'])
def coins_page():
    # Handle POST request when user submits a search query
    if request.method == "POST":
        # Retrieve the search query from the form
        search_query = request.form.get('search_query')
        the_query =  f"SELECT url FROM coins WHERE name = '{search_query}'"
        queries = the_query.split(';')

        if ";"in search_query or "'" in search_query:
            app.logger.info(f"SQL Injection attack tried by query: {search_query}")  

        # Iterate through the queries
        for query in queries:
            if query == '--':
                pass
            if '%s' in query:
                # Execute the query with placeholder
                cursor.execute(query, (search_query,))
            else:
                # Execute the query without placeholder
                cursor.execute(query)
            if "insert" in query.lower():
                mysql.commit()
        # Log the executed query for auditing purposes
        app.logger.info(f"Query executed: {the_query}")

        # Fetch all matching results for the query
        search_results = cursor.fetchall()

        # If there are results, redirect to the first result's URL; otherwise, return an error message
        if search_results:
            return redirect(search_results[0][0])
        else:
            return "Coin not found"

    # If method is GET, display all coins
    cursor.execute("SELECT id, name FROM coins")
    all_coins = cursor.fetchall()

    # Render the coins page with the list of all coins, customizing the username based on authentication status
    if current_user.is_authenticated:
        return render_template('coins.html', username=current_user.username, all_coins=all_coins)
    else:
        return render_template('coins.html', username='Misafir',  all_coins=all_coins)

# Define the route for the coins page which allows users to search for coins
@app.route("/economists", methods=['POST', 'GET'])
def economists_page():
    # Handle POST request when user submits a search query
    if request.method == "POST":
        # Retrieve the search query from the form
        search_query = request.form.get('search_query')
        # Construct a SQL query to find the coin by name
        the_query =  f"SELECT * FROM economists WHERE name = '{search_query}'"
        
        # Attempt to protect against SQL injection by splitting and executing only the first command
            
        queries = the_query.split(';')

        # Iterate through the queries
        for query in queries:
            if query == '--':
                pass
            if '%s' in query:
                # Execute the query with placeholder
                cursor.execute(query, (search_query,))
            else:
                # Execute the query without placeholder
                cursor.execute(query)
            if "insert" in query.lower():
                mysql.commit()

        
        # Log the executed query for auditing purposes
        app.logger.info(f"Query executed: {the_query}")

        # Fetch all matching results for the query
        search_results = cursor.fetchall()

        # If there are results, redirect to the first result's URL; otherwise, return an error message
        if search_results:
            return redirect(search_results[0][0])
        else:
            return "Economist not found"

    # If method is GET, display all coins
    cursor.execute("SELECT * FROM economists")
    all_economists = cursor.fetchall()

    # Render the coins page with the list of all coins, customizing the username based on authentication status
    if current_user.is_authenticated:
        return render_template('economists.html', username=current_user.username, all_economists=all_economists)
    else:
        return render_template('economists.html', username='Misafir',  all_economists=all_economists)



# Define a route to log out the current user
@app.route('/logout')
@login_required  # Ensures that the user is logged in before allowing them to log out
def logout():
    logout_user()  # Logout the user using flask_login's logout_user method
    flash('Çıkış Başarılı!', 'success')  # Flash a success message indicating a successful logout
    return redirect(url_for('main_page'))  # Redirect to the main page after logging out

# Define a route to delete a user by an admin
@app.route('/delete_user/<int:user_id>', methods=['POST'])
@login_required  # Ensures that the user is logged in before accessing this route
def delete_user(user_id):
    # Check if the current user is an admin
    if not current_user.is_admin():
        # Log unauthorized access attempts and render an access denied page
        app.logger.info("User tried to reach forbidden page.")
        return render_template('access_denied.html')
    
    # If authorized, delete the user by their ID
    delete_user_by_id(user_id)

    # Redirect to the admin page after deletion
    return redirect(url_for('admin'))

# Define a route to delete a comment by an admin
@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
@login_required  # Ensures that the user is logged in before accessing this route
def delete_comment(comment_id):
    # Check if the current user is an admin
    if not current_user.is_admin():
        # Log unauthorized access attempts and render an access denied page
        app.logger.info("User tried to reach forbidden page.")
        return render_template('access_denied.html')
    
    # If authorized, delete the comment by its ID
    delete_comment_by_id(comment_id)

    # Redirect to the admin page after deletion
    return redirect(url_for('admin'))

# Define a route to add a comment
@app.route('/add_comment', methods=['POST'])
@login_required  # Ensures that the user is logged in before accessing this route
def add_comment():
    # Check if the incoming request is a POST request
    if request.method == 'POST':
        # Retrieve data from the form submitted
        current_route = request.form.get('current_route')
        message = request.form.get('message')
        news_link = request.form.get('news_link')

        # Check for potential stored XSS attack in the message
        if "<" in message or ">" in message:
            app.logger.info(f"Stored XSS attack on comment: {message}")
        
        # Ensure message is not empty
        if not message:
            flash('Yorum boş olamaz!', 'error')  # Send an error message to the user
            return redirect(current_route)  # Redirect back to the current route

        # Process and store the comment data in the database, including the news link
        query = 'INSERT INTO comments (username, content, news_link) VALUES (%s, %s, %s)'
        cursor.execute(query, (current_user.username, message, news_link))
        mysql.commit()  # Commit changes to the database

        flash('Yorum başarılı bir şekilde kaydedildi!', 'success')  # Send a success message

        # Redirect back to the original news article page
        return redirect(request.referrer)  # Referrer is the previous URL from which the POST request was made


# Define a route for displaying a single news article, using <keyword> as a dynamic segment
@app.route("/single.html/<keyword>")
def single_news_page(keyword):
    # Fetch comments related to the current news link
    query = 'SELECT * FROM comments WHERE news_link = %s'

    cursor.execute(query, ("/single.html/"+keyword,))
    comment_data = cursor.fetchall()  # Fetching all comments related to the article

    # Fetch the single news item using the provided keyword
    news = get_single_news(keyword)
    
    # Extracting and preparing news details for the HTML template
    subject = 'Ekonomi'
    title = news.title
    length = len(title)
    image_src = news.links[0]['href']  # Link to the news image
    source_url = news.link  # Original link to the news article
    redirected_url = "http://127.0.0.1:5000/redirect?url=" + source_url  # URL for the redirect route
    description = news.description[length+1:]  # News description
    content = news.content[0]['value']  # Main content of the news
    date = news.published  # Publication date

    # Create Comment objects from the retrieved data for rendering
    comments = [Comment(*row) for row in comment_data]

    # Check if the current user is authenticated to customize the rendered page
    if current_user.is_authenticated:
        return render_template('single.html', 
                               username=current_user.username, 
                               comments=comments, 
                               current_news_link=request.path,
                               title=title,
                               subject=subject,
                               image_src=image_src,
                               description=description,
                               content=content,
                               date=date,
                               redirected_url=redirected_url
                            )
    else:  # Default rendering for guests (non-authenticated users)
        return render_template('single.html', 
                            username='Misafir',
                            comments=comments, 
                            current_news_link=request.path,
                            title=title,
                            subject=subject,
                            image_src=image_src,
                            description=description,
                            content=content,
                            date=date,
                            redirected_url=redirected_url
                        )


# Define a route for handling redirection to external news sources
@app.route("/redirect")
def redirect_page():
    # Fetch the URL parameter to redirect to
    url = request.args.get('url', '')
    
    # Log if the redirect URL is not validated for expected domain
    if "www.ekonomidunya.com" not in url:
        app.logger.info(f"Unvalidated redirect: {url}")
    
    # Render the redirection page, customizing the username based on authentication status
    if current_user.is_authenticated:
        return render_template('redirect.html', username=current_user.username)
    else:
        return render_template('redirect.html', username='Misafir')


# Check if the script is the main program and run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode for development purposes


    