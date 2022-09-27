from flask_restx import Namespace, Resource
from flask import request
from app.dao.genre_dao import GenreDAO
from app.dao.models import Genre, GenreSchema


genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
genres_dao = GenreDAO(Genre, GenreSchema)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Получаем список всех жанров"""
        genres = genres_dao.get_all()
        return genres, 200

    def post(self):
        """Добавление жанра"""
        req_json = request.json
        genres_dao.add_genre(req_json)
        return f" Жанр {req_json['name']} добавлен", 201


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        """Возвращает жанр по id"""
        genre = genres_dao.get_genre_by_id(uid)
        if type(genre) != dict:
            return genre, 404
        return genre, 200

    def put(self, uid):
        """Обновляет жанр по id"""
        req_json = request.json
        print(type(req_json))
        genres_dao.put_genre(uid, req_json)
        return f" Жанр {req_json['name']} обновлен", 200

    def delete(self, uid):
        """Удаляет жанр по id"""
        genres_dao.delete_genre(uid)
        return "", 204

