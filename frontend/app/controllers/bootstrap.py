from app import app
from flask import render_template, flash, redirect, url_for
from flask_pymongo import PyMongo

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)