from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


def init_app():

    # config route
    from app.routes.user_route import user_bp
    app.register_blueprint(user_bp)

    return app
