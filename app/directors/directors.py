from flask_restx import Namespace, Resource
from app.dao.models import GenreSchema

director_ns = Namespace('directors')

director_schema = GenreSchema()
directors_schema = GenreSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """Возвращает список всех режиссеров"""
        return "", 200

    def post(self):
        """Доюовляет режиссера"""
        return "", 201


@director_ns.route('/<int:id>')
class DirectorView(Resource):
    def get(self, id):
        """Возвращает режиссера по id"""
        return "", 200

    def put(self, id):
        """Обновляет режиссера по id"""
        return "", 200

    def delete(self, id):
        """Удаляет режиссера по id"""
        return "", 204
