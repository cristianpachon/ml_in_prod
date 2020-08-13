from flask import Flask, render_template, request
from forms import InputFeatures

app = Flask(__name__)

app.config['SECRET_KEY'] = '5ea24f645f63b6f9316f899c8da889cd'

@app.route('/')
def index():
    form = InputFeatures()
    return render_template('index.html', form=form)


@app.route('/your_name', methods = ['POST'])
def display_name(name=None):
    form = InputFeatures(request.form)
    name = form.username.data
    if name is None:
        name = 'Loser'
    return render_template('display_name.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
