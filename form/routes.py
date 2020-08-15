from form import app
from form.forms import InputFeatures
from flask import Flask, render_template, request, redirect, url_for, session

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputFeatures()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for('display_name'))
    else:
        return render_template('index.html', form=form)

@app.route('/display_name', methods = ['GET', 'POST'])
def display_name():
    try:
        name = session['username']
    except:
        name = 'Loser'
    return render_template('display_name.html', name=name)