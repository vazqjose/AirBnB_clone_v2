#!/usr/bin/python3
'''
Write a script that starts a Flask web application
'''


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ display “Hello HBNB!” """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB” """

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    ''' display “C ” followed by the text variable '''

    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text='is cool'):
    '''The default value of text is “is cool” '''

    text = text.replace("_", " ")
    return "Python " + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
