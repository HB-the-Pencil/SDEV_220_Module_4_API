from flask import flask, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hi"
