from flask_restx import Namespace, Resource
from flask import request

from app.dao.director_dao import DirectorDAO
from app.dao.models import DirectorSchema, Director

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

director_dao = DirectorDAO(Director, DirectorSchema)


@director_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Получаем список всех режиссеров"""
        genres = director_dao.get_all()
        return genres, 200

    def post(self):
        """Добавление режиссера"""
        req_json = request.json
        director_dao.add_director(req_json)
        return f" Режиссер {req_json['name']} добавлен", 201


@director_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        """Возвращает режиссера по id"""
        genre = director_dao.get_director_by_id(uid)
        if type(genre) != dict:
            return genre, 404
        return genre, 200

    def put(self, uid):
        """Обновляет режиссера по id"""
        req_json = request.json
        print(type(req_json))
        director_dao.put_director(uid, req_json)
        return f" Режиссер {req_json['name']} обновлен", 200

    def delete(self, uid):
        """Удаляет режиссера по id"""
        director_dao.delete_director(uid)

