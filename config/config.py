import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


load_dotenv()
DB_USER = os.getenv("DB_USER", 'default_user')
DB_PASSWORD = os.getenv("DB_PASSWORD", 'default_password')
DB_HOST = os.getenv("DB_HOST", "default_host")
DB_PORT = os.getenv("DB_PORT", "default_port")
DB_NAME = os.getenv("DB_NAME", "default_name")
DB_ENGINE = os.getenv("DB_ENGINE", "postgresql")

DB_URI = f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


class Config:
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


# Select the config based on environment variable
config_options = {
    "DEV": DevConfig,
    "PROD": ProductionConfig,
}

# Default to development if FLASK_ENV is not set
ConfigClass = config_options.get(os.getenv("FLASK_ENV", "DEV"))
