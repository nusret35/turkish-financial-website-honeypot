from flask import Flask, render_template
from fetch_rss import news_feed_html

app = Flask("cs437-project")

@app.route("/index.html")
def main_page():
    news_html_content = news_feed_html()
    return render_template('index.html',news_html_content=news_html_content)


@app.route("/category.html")
def category_page():
    return render_template('category.html')

@app.route("/contact.html")
def contact_page():
    return render_template('contact.html')

@app.route("/single.html")
def single_news_page():
    return render_template('single.html')

if __name__ == '__main__':
    app.run(debug=True)