from flask_restx import Namespace, Resource
from app.models import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """Возвращает список всех жанров"""
        return "", 200

    def post(self):
        """Доюовляет жанр"""
        return "", 201


@genre_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        """Возвращает жанр по id"""
        return "", 200

    def put(self, id):
        """Обновляет жанр по id"""
        return "", 200

    def delete(self, id):
        """Удаляет жанр по id"""
        return "", 204

