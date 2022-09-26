import json
from app.setup_db import db


class MovieDAO:

    def __init__(self, model, schema):
        """Получает модель и схему"""
        self.model = model
        self.schema = schema

    def get_all(self) -> list[dict]:
        """Возвращает список всех данных"""
        movies = self.model.query.all()
        return self.schema(many=True).dump(movies)

    def add_movie(self, data):
        """Получаем json, добавляем новый фильм в бд"""
        model = self.model
        movie = model(**data)
        with db.session.begin():
            db.session.add(movie)

    def put_movie(self, data):
        """Обновляет фильм"""


