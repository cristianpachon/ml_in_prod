from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/your_name', methods = ['POST'])
def patata(name=None):
    name = request.form.get('content')
    if name is None:
        name = 'Loser'
    return render_template('display_name.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)