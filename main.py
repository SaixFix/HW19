from flask import Flask
from flask_restx import Api

from app.config import Config
# from app.directors.directors import director_ns
# from app.genre.genres import genre_ns
from app.movie.movies import movie_ns
from app.setup_db import db


def create_app(config: Config) -> Flask:
    aplication = Flask(__name__)
    aplication.config.from_object(config)
    aplication.app_context().push()
    return aplication


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    # api.add_namespace(director_ns)
    # api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)


if __name__ == '__main__':
    app = create_app(Config())
    configure_app(app)
    app.run()



