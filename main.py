from flask import Flask
from flask_restx import Api

from app.setup_db import db

from app.config import Config
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.users import user_ns
from app.views.auth import auth_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(auth_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)


app = create_app(Config())
configure_app(app)

if __name__ == '__main__':
    app.run(debug=True)
