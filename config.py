from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
DEFAULT_DB_FILE = "sqlite:///{}".format(path.join(basedir, "moviestrore.db"))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Flask Config
    SECRET_KEY = environ.get('SECRET_KEY', 'test')
    FLASK_ENV = environ.get('FLASK_ENV', 'production')
    DEBUG = environ.get('DEBUG', True)
    FLASK_APP = 'wsgi.py'
    FLASK_PORT = environ.get('FLASK_PORT', True)
    FLASK_HOST = environ.get('FLASK_HOST', "0.0.0.0")

    # Database stuff
    # default to local if not set
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI", DEFAULT_DB_FILE)
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
