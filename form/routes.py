from form import app
from form.forms import InputFeatures
from flask import Flask, render_template, redirect, url_for, session
from model.get_prediction import get_prediction
import logging
import logging.config
import yaml

# Logging initialisation
with open('logging.yaml', 'r') as f:
    log_cfg = yaml.safe_load(f.read())
    logging.config.dictConfig(log_cfg)
    logger = logging.getLogger('simpleExample')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputFeatures()
    if form.validate_on_submit():
        session['median_age'] = form.median_age.data
        return redirect(url_for('display_info'))
    else:
        logger.info('Rendenring index')
        return render_template('index.html', form=form)

@app.route('/display_info', methods = ['GET', 'POST'])
def display_info():
    logger.info('Displaying prediction')
    median_age = session['median_age']
    features = {'median_age':median_age}
    price = get_prediction(features)[0][0]
    return render_template('display_info.html', median_age=median_age, price=price)
