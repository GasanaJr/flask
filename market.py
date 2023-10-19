"""Market application in Flask"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    """Function to return the homepage"""
    return render_template('home.html')


@app.route('/market')
def market_page():
    """Function to return market page"""
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)


# @app.route('/about/<username>')
# def last_king(username):
#     """Description of The app"""
#     return f'<h1>This is the about page of {username}</h1>'
