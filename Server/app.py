from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f'<h1>Hello from Flask servername</h1>'
####

@app.route("/name")
def name():
    return f'<h1>You are on name page</h1>'