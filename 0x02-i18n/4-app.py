#!/usr/bin/env python3
"""a way to force a particular locale by passing
the locale=fr parameter to your app’s URLs"""

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
    return render_template("4-index.html")


@babel.localeselector
def get_locale():
    """method that determines best supported languages"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
