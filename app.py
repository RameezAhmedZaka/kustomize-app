from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Welcome to the Fancy Flask App!</h1>
    <ul>
        <li><a href='/a'>Go to Page A</a></li>
        <li><a href='/b'>Go to Page B</a></li>
        <li><a href='/prod-a'>Go to Prod A</a></li>
        <li><a href='/prod-b'>Go to Prod B</a></li>
    </ul>
    """

@app.route("/a")
def page_a():
    return "<h2>✅ This is Page A</h2>"

@app.route("/b")
def page_b():
    return "<h2>✅ This is Page B</h2>"

@app.route("/prod-a")
def prod_a():
    return "<h2>🏭 Production A Route</h2>"

@app.route("/prod-b")
def prod_b():
    return "<h2>🏭 Production B Route</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

