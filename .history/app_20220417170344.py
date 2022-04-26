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
    conn = sqlite3.connect('myScrapedDatabase.db')
    cursor = conn.cursor()
    if request.method == "POST":
        # search by author or book
        cursor.execute("SELECT * FROM titlesFavorites")
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        return render_template('search.html', data=data)
    return render_template('search.html')
@app.route('/results')
def results():
    return render_template('results.html')
# create route named google that will accept search term from the user
@app.route('/google')
def google():
    return render_template('google.html')
if __name__ == '__main__':
    app.run(debug=True)