from flask import render_template

from app import app  # Our app.py file
import forms


@app.route('/')
@app.route('/Home')
def index():
    return render_template('index.html')


@app.route('/About')
def about():
    form = forms.AddTask()
    return render_template('about.html', form=form)
