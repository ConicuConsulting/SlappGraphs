import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("DEBUG", True)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///agn.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
