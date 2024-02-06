#!/usr/bin/env python3
"""
Flask app with Babel extension for internationalization.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)

class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """
    Determine the best-matching language based on request.accept_languages.

    :return: The selected language.
    """
    forced_locale = request.args.get('locale')
    if forced_locale and forced_locale in app.config['LANGUAGES']:
        return forced_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    Route for the home page.

    :return: Rendered template with title and header.
    """
    return render_template('4-index.html', title=_("home_title"), header=_("home_header"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
