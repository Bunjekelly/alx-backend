#!/usr/bin/env python3
"""a get_locale function with the babel.localeselector
decorator. Use request.accept_languages to determine the best
match with our supported languages."""

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """class congig"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def hello():
    """returns the html template"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """method that determines best supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True)
