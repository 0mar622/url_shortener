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
    data = request.json
    long_url = data.get('long_url')
    custom_code = data.get('custom_code')  # optional custom short code

    # validate URL
    from urllib.parse import urlparse
    parsed = urlparse(long_url)
    if not (parsed.scheme and parsed.netloc):
        return {"error": "Invalid URL. Please include http:// or https://"}, 400

    conn = get_db_connection()
    c = conn.cursor()

    # create table if not exists
    c.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        short_code TEXT UNIQUE,
        long_url TEXT NOT NULL,
        clicks INTEGER DEFAULT 0
    )
    """)

    # check if this URL already exists
    c.execute("SELECT short_code FROM urls WHERE long_url = ?", (long_url,))
    existing = c.fetchone()
    if existing:
        conn.close()
        return {"short_url": f"http://127.0.0.1:5000/{existing['short_code']}"}

    # if user provided custom code, use it (if not taken)
    if custom_code:
        c.execute("SELECT 1 FROM urls WHERE short_code = ?", (custom_code,))
        if c.fetchone():
            conn.close()
            return {"error": "Custom code already taken. Please choose another."}, 400
        short_code = custom_code
    else:
        # otherwise generate random 6-character short code
        import string, random
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
    app.run(debug=True)     # run the main 2
