from flask import render_template

from app import app  # Our app.py file


@app.route('/')
@app.route('/Home')
def index():
    return render_template('index.html')


@app.route('/About')
def about():
    return render_template('about.html')
