from flask import render_template, redirect, url_for
from datetime import datetime
from app import app, db  # Our app.py file
from models import Task  # Our models.py file
import forms


@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTask()
    if form.validate_on_submit():
        task = Task(title=form.title.data , date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)
