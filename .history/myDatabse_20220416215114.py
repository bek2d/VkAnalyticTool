import sqlite3
from sqlite3 import Error
from scraped import article_title


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


if __name__ == '__main__':
    conn = create_connection("myScrapedDatabse.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS titlesFavorites (title TEXT)""")
    for i in range(len(article_title)):
        c.execute("INSERT INTO titlesFavorites VALUES (?)",
                  (article_title[i],))
    conn.commit()
    conn.close()
