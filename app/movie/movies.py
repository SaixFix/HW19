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
        print(req_json)
        print(type(req_json['rating']))
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




    def put(self, id):
        """Обновление фильма по id"""
        return "", 200

    def delete(self, id):
        """Удаление по id"""
