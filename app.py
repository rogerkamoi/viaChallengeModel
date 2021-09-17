from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/mike')
def mike():
    return "Hello World Mike"


if __name__ == '__main__':
    app.run(debug=True)
