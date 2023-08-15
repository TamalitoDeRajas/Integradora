import os

class Config(object):
    SECRET_KEY = 'equiporeest'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = '20203tn144@utez.edu.mx'
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:Admin123@databasehector.cizk8twbs3se.us-east-1.rds.amazonaws.com/final'    
    SQLALCHEMY_TRACK_MODIFICATIONS = False