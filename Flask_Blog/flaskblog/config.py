import os


class Config:
    SECRET_KEY = 'd9kjdjf4b6l2weg98kjdjf4h8d2iweg'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = <Email id through which you want to send mails >
    MAIL_PASSWORD = <Password for same >
