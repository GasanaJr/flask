from marketPackage import app
from flask import render_template, redirect, url_for, flash
from marketPackage.models import Item, User
from marketPackage.forms import RegisterForm, LoginForm
from marketPackage import db


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['get', 'post'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password_hash=form.password1.data)
        with app.app_context():
            db.session.add(user_to_create)
            db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"An error occurred: {err_msg}", category='danger')
    return render_template('register.html', form=form)


@app.route('/login')
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)
