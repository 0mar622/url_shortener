from flask import Flask, request, redirect

app = Flask(__name__)

# In-memory storage for now
url_map = {}

@app.route('/')
def home():
    return "Hello, URL Shortener!"

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.json['long_url']   # get URL from request body
    short_code = str(len(url_map) + 1)    # simple code: "1", "2", "3", ...
    url_map[short_code] = long_url        # save mapping
    return {"short_url": f"http://127.0.0.1:5000/{short_code}"}

@app.route('/<short_code>')
def redirect_to_url(short_code):
    long_url = url_map.get(short_code)
    if long_url:
        return redirect(long_url)
    return {"error": "URL not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
