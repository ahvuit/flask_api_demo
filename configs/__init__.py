import os

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")


class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + db_user + ":" + db_pass + '@' + db_host + '/' + db_name
    SQLALCHEMY_TRACK_MODIFICATIONS = False
