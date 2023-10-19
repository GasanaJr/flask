"""Market application in Flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """Function to print hello world"""
    return '<h1>Junior Last King</h1>'


# @app.route('/about/<username>')
# def last_king(username):
#     """Description of The app"""
#     return f'<h1>This is the about page of {username}</h1>'
