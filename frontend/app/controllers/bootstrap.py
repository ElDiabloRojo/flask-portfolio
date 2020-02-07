from app import app
from flask import render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from app.forms.forms import LoginForm


mongo = PyMongo(app)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)