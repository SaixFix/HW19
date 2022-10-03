from flask_restx import Namespace, Resource
from flask import request

from app.container import genre_service
from app.dao.models.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Получаем список всех жанров"""
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200

    def post(self):
        """Добавление жанра"""
        req_json = request.json
        genre_service.add_genre(req_json)
        return f" Жанр {req_json['name']} добавлен", 201


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        """Возвращает жанр по id"""
        genre = genre_service.get_genre_by_id(uid)
        if type(genre) != dict:
            return genre, 404
        return genre_schema.dump(genre), 200

    def put(self, uid):
        """Обновляет жанр по id"""
        req_json = request.json
        print(type(req_json))
        genre_service.put_genre(uid, req_json)
        return f" Жанр {req_json['name']} обновлен", 200

    def delete(self, uid):
        """Удаляет жанр по id"""
        genre_service.delete_genre(uid)
        return "", 204

