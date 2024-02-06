#!/usr/bin/env python3
"""
Flask app with Babel extension for internationalization.
"""
from flask import Flask, render_template, request, g
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

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """
    Get user information based on user ID.

    :param user_id: ID of the user.
    :return: User dictionary or None if not found.
    """
    return users.get(user_id)

@babel.localeselector
def get_locale():
    """
    Determine the best-matching language based on user preferences and request.

    Priority:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale

    :return: The selected language.
    """
    # 1. Locale from URL parameters
    forced_locale = request.args.get('locale')
    if forced_locale and forced_locale in app.config['LANGUAGES']:
        return forced_locale

    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.before_request
def before_request():
    """
    Set the user in Flask's global context (g) based on the login_as parameter.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

@app.route('/')
def index():
    """
    Route for the home page.

    :return: Rendered template with a welcome message or a default message.
    """
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
