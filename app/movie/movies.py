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
        movie_dao.add_movie(req_json)
        return f" Фильм {req_json['title']} добавлен", 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        """Получаем фильм по id"""
        movie = movie_dao.get_film_by_id(uid)
        if type(movie) != dict:
            return movie, 404
        return movie, 200

    def put(self, uid):
        """Обновление фильма по id"""
        req_json = request.json
        print(type(req_json))
        movie_dao.put_movie(uid, req_json)
        return f" Фильм {req_json['title']} обновлен", 200

    def delete(self, uid):
        """Удаление по id"""
        movie_dao.delete_film(uid)
        return "", 204

