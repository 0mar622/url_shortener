from flask import Flask, request, redirect
import os; print("DB path:", os.path.abspath("urls.db"))
import sqlite3
import string, random
from urllib.parse import urlparse

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

    # generate random 6-character short code
    chars = string.ascii_letters + string.digits
    short_code = ''.join(random.choices(chars, k=6))

    # insert mapping into DB
    c.execute("INSERT INTO urls (short_code, long_url) VALUES (?, ?)", (short_code, long_url))
    conn.commit()
    conn.close()

    # use dynamic host URL
    return {"short_url": f"{request.host_url}{short_code}"}


@app.route('/<short_code>')
def redirect_to_url(short_code):
    conn = get_db_connection()
    c = conn.cursor()

    # find long_url for given short_code
    c.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    row = c.fetchone()

    if row:
        # increment click counter
        c.execute("UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?", (short_code,))
        conn.commit()
        conn.close()
        return redirect(row[0])

    conn.close()
    return {"error": "URL not found"}, 404


@app.route('/stats')
def stats():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT short_code, long_url, clicks FROM urls")
    rows = c.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            "short_code": row[0],
            "long_url": row[1],
            "clicks": row[2]
        })
    return {"stats": data}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # run the main
