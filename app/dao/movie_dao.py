from app.setup_db import db


class MovieDAO:

    def __init__(self, model, schema, session):
        """Получает модель, схему и сессию"""
        self.session = session
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
        self.session.add(movie)
        self.session.commit()

    def put_movie(self, uid: int, data: dict):
        """Обновляет фильм"""
        model = self.model
        movie = model.query.filter(model.id == uid).one()

        if "genre_id" in data:
            movie.genre_id = data.get("genre_id")
        if "year" in data:
            movie.year = data.get("year")
        if "title" in data:
            movie.title = data.get("title")
        if "rating" in data:
            movie.rating = data.get("rating")
        if "director_id" in data:
            movie.director_id = data.get("director_id")
        if "trailer" in data:
            movie.trailer = data.get("trailer")
        if "description" in data:
            movie.description = data.get("description")

        db.session.add(movie)
        db.session.commit()

    def get_film_by_id(self, uid: int) -> dict:
        """Получаем фильм по id либо ошибка в str"""
        model = self.model
        schema = self.schema
        try:
            movie = model.query.filter(model.id == uid).one()
            return schema().dump(movie)
        except Exception as error:
            return str(error)

    def delete_film(self, uid: int):
        """Удаляем фильм по id"""
        model = self.model
        movie = model.query.filter(model.id == uid).one()
        db.session.delete(movie)
        db.session.commit()







