import sqlite3
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# @app.route('/')
# def index():
#     conn = sqlite3.connect('myScrapedDatabase.db')
#     posts = conn.execute('SELECT * FROM titlesFavorites').fetchall()
#     conn.close()
#     return render_template('index.html', posts=posts)


# @app.route('/about')
# def about():
#     conn = sqlite3.connect('myScrapedDatabase.db')
#     posts = conn.execute('SELECT * FROM titlesFavorites').fetchall()
#     conn.close()
#     return str(posts)
# # run flask app



#endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')
@app.route('/results', methods=['GET', 'POST'])
def results():
    conn = sqlite3.connect('myScrapedDatabase.db')
    cursor = conn.cursor()
    book = request.form.get('title')
    cursor.execute("SELECT * FROM titlesFavorites WHERE title LIKE ?", (book,))
    conn.commit()
    data = cursor.fetchall()
    return render_template('results.html', data=data)
# create route named google that will accept search term from the user
@app.route('/google')
def google():
    return render_template('google.html')
if __name__ == '__main__':
    app.run(debug=True)