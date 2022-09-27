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

    def add_movie(self, data: dict):
        """Получаем json, добавляем новый фильм в бд"""
        model = self.model
        movie = model(**data)
        with db.session.begin():
            db.session.add(movie)

    def put_movie(self, uid: int, data: dict):
        """Обновляет фильм"""
        model = self.model
        movie = model.query.filter(model.id == uid).one()

        if "genre_id" in data:
            model.genre_id = data.get("title")
        if "year" in data:
            model.year = data.get("year")
        if "title" in data:
            model.year = data.get("title")
        if "rating" in data:
            model.year = data.get("rating")
        if "director_id" in data:
            model.year = data.get("director_id")
        if "trailer" in data:
            model.year = data.get("trailer")
        if "description" in data:
            model.year = data.get("description")

        with db.session.begin():
            db.session.add(movie)

    def get_film_by_id(self, uid: int) -> dict:
        """Получаем фильм по id либо ошибка в str"""
        model = self.model
        schema = self.schema
        try:
            movie = model.query.filter(model.id == uid).one()
            return schema().dump(movie)
        except Exception as error:
            return str(error)






