#!/usr/bin/env python3
"""
Flask app with Babel extension for internationalization.
"""
from flask import Flask, render_template
from flask_babel import Babel

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

@app.route('/')
def index():
    """
    Route for the home page.

    :return: Rendered template with title and header.
    """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
