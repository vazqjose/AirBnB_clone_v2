#!/usr/bin/python3
'''
Write a script that starts a Flask web application
'''


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    ''' Says hello by default '''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' 1st option of route '''

    return "HBNB"


if __name__ == "__main__":
    ''' runs the program '''

    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
