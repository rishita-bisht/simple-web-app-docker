from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "You're home now!"

@app.route("/hello-world")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    # debug=True is handy while developing
    app.run(debug=True, host="0.0.0.0", port=5001)

