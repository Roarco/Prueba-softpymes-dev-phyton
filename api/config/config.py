
# -*- coding: utf-8 -*-
#########################################################
import os
from dotenv import load_dotenv
from pathlib import Path 


class Config:
    """
    Flask configurations
    """
    load_dotenv()
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    ENV = 'development'
    DEBUG = True if int(os.getenv('DEBUG')) else False
    # Content Length 50 Mb
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024

    """
    SQLAlchemy configurations
    """
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
        os.getenv("MYSQL_USER"),
        os.getenv("MYSQL_PASSWORD"),
        os.getenv("MYSQL_HOST"),
        os.getenv("MYSQL_PORT"),
        os.getenv("MYSQL_DATABASE")
    )

    ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
