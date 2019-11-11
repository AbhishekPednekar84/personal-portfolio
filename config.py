import os
import dotenv

dotenv.load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class DevConfig(Config):
    DEBUG = True
