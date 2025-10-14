from flask import Flask, request, redirect
import os; print("DB path:", os.path.abspath("urls.db"))
import sqlite3
import string, random

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("urls.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "Hello, URL Shortener is here!"

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.json['long_url']
    conn = get_db_connection()
    c = conn.cursor()

    # create table if not exists
    c.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short_code TEXT UNIQUE,
        long_url TEXT NOT NULL
    )
    """)

    # generate random 6-character short code
    chars = string.ascii_letters + string.digits
    short_code = ''.join(random.choices(chars, k=6))

    # insert mapping into DB
    c.execute("INSERT INTO urls (short_code, long_url) VALUES (?, ?)", (short_code, long_url))
    conn.commit()
    conn.close()

    return {"short_url": f"http://127.0.0.1:5000/{short_code}"}

@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    row = c.fetchone()
    conn.close()

    if row:
        return redirect(row[0])
    return {"error": "URL not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)     # run the main 2
