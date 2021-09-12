#!/usr/bin/python3
'''
    Write a script that starts a Flask web application,
    must be listening on 0.0.0.0, port 5000
'''


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ display “Hello HBNB!” """

    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display “HBNB” """

    return "HBNB"


@app.route('/c/<text>')
def c(text):
    ''' display “C ” followed by the text variable '''

    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def py(text='is cool'):
    '''The default value of text is “is cool” '''

    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    ''' Display only if integer '''

    if isinstance(n, int):
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def template(n):
    ''' display a HTML page only if n is an integer '''

    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    res = 0
    if isinstance(n, int):
        if n % 2 == 0:
            res = "even"
        else:
            res = "odd"

        return render_template(
                '6-number_odd_or_even.html', number=n, evenodd=res)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
