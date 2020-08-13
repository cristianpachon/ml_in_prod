from flask import Flask, render_template, request, redirect, url_for
from forms import InputFeatures

app = Flask(__name__)

app.config['SECRET_KEY'] = '5ea24f645f63b6f9316f899c8da889cd'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputFeatures()
    if form.validate_on_submit():
        return redirect(url_for('display_name'))
    else:
        return render_template('index.html', form=form)

@app.route('/display_name', methods = ['POST'])
def display_name():
    try:
        name = request.form.get('username')
    except:
        name = 'Loser'
    return render_template('display_name.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
