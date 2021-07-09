from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/thing/<name>')
def say_things(name):
    return 'Hi ' + str(name)


@app.route('/repeat/<num>/<stuff>')
def num_str(num, stuff):
    return str(stuff + ' ') * int(num)


@app.errorhandler(404)
def error(error):
    return "Sorry! No response. Try again"


if __name__ == "__main__":
    app.run(debug=True)
