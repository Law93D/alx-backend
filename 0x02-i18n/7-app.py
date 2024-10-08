#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from datetime import datetime
import pytz


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    g.user = get_user()


@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    timezone = request.args.get('timezone')
    if timezone:
        try:
            return pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            return pytz.timezone(g.user['timezone'])
        except pytz.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    current_time = (
            datetime.now(get_timezone()).strftime('%Y-%m-%d %H:%M:%S %Z%z')
        )
    return render_template('7-index.html', current_time=current_time)


if __name__ == '__main__':
    app.run()
