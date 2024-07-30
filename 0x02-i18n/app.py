#!/usr/bin/env python3
"""
Flask app module with i18n support.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Configuration class for Flask-Babel.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Get the user from the mock database.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Before request handler to get user.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Get the best match locale.
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in Config.LANGUAGES:
            return user_locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    """
    Get the best match timezone.
    """
    timezone_param = request.args.get('timezone')
    if timezone_param:
        try:
            return pytz.timezone(timezone_param).zone
        except UnknownTimeZoneError:
            pass
    if g.user:
        user_timezone = g.user.get('timezone')
        try:
            return pytz.timezone(user_timezone).zone
        except UnknownTimeZoneError:
            pass
    return Config.BABEL_DEFAULT_TIMEZONE


@app.route('/')
def index():
    """
    Index route.
    """
    current_time = datetime.now(timezone(get_timezone()))
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True)
