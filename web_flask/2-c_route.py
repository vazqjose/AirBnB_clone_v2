#!/usr/bin/python3
'''
Write a script that starts a Flask web application
'''


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    ''' default greet '''

    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' greet with hbnb '''
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    ''' replaces _ with spaces in string '''

    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
