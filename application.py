from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.name} by {self.author}"

@app.route('/')
def index():
    return "hi"

@app.route('/books')
def get_books():
    books = {
        "Harry Potter and the Sorcerer's Stone": "JK Rowling",
        "The Lord of the Rings": "JRR Tolkien",
    }
    return books

if __name__ == '__main__':
    app.run(debug=True)
