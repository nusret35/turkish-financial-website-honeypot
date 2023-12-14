from flask import Flask, render_template

app = Flask("cs437-project")

@app.route("/index.html")
def main_page():
    return render_template('index.html')


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