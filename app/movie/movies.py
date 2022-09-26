from flask_restx import Namespace, Resource
from app.dao.models import Movie, MovieSchema
from app.dao.movie_dao import MovieDAO
from flask import request

movie_ns = Namespace('movies')

movie_dao = MovieDAO(Movie, MovieSchema)




@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Получаем список всех фильмов"""
        movies = movie_dao.get_all()
        return movies, 200

    def post(self):
        """Добавление фильма"""
        req_json = request.json
        print(type(req_json))
        movie_dao.add_movie(**req_json)

        return "", 201


@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        """Получаем фильм по id"""
        try:
            movie = Movie.query.filter(Movie.id == id).one()
            return movie_schema.dump(movie), 200
        except Exception as error:
            return str(error), 404

    def put(self, id):
        """Обновление фильма по id"""
        return "", 200

    def delete(self, id):
        """Удаление по id"""
