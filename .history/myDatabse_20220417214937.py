import sqlite3
from sqlite3 import Error
from scraped import ids


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)


if __name__ == '__main__':
    conn = create_connection("myScrapedDatabse.db")
    c = conn.cursor()
    #create sqlite table
    c.execute("""CREATE TABLE IF NOT EXISTS jsonIDs(id text)""")
    for i in range(len(ids)):
        c.execute("INSERT INTO titlesFavorites VALUES (?)",
                  (ids[i],))
    conn.commit()
    conn.close()
