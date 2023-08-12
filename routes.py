from flask import render_template, redirect, url_for, flash, get_flashed_messages
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
        task = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(task)
        db.session.commit()
        flash('A new task added successfully!')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.EditTask()
    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task edited successfully!')
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    flash(f'Task with id {task_id} does not exist.')
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTask()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task deleted successfully!')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    flash(f'Task with id {task_id} does not exist.')
    return redirect(url_for('index'))


@app.route('/delete_all', methods=['GET', 'POST'])
def delete_all():
    form = forms.DeleteAll()
    tasks = Task.query.all()
    if form.validate_on_submit():
        if tasks:
            num_rows_deleted = Task.query.delete()
            db.session.commit()
            if num_rows_deleted == 1:
                flash(f'{num_rows_deleted} task deleted successfully!')
            else:
                flash(f'{num_rows_deleted} tasks deleted successfully!')
            return redirect(url_for('index'))
        flash('No tasks to delete yet!.')
        return redirect(url_for('index'))
    return render_template('delete_all.html', form=form)
