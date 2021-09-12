#!/usr/bin/python3
'''
Write a script that starts a Flask web application
'''


from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    ''' says hello HBNB! by default '''

    return "Hello HBNB!"


if __name__ == "__main__":
    ''' call the program '''

    app.debug = True
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
