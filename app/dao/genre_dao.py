from app.setup_db import db


class GenreDAO:

    def __init__(self, model, schema):
        """Получает модель и схему"""
        self.model = model
        self.schema = schema

    def get_all(self) -> list[dict]:
        """Возвращает список всех данных"""
        genres = self.model.query.all()
        return self.schema(many=True).dump(genres)

    def add_genre(self, data: dict):
        """Получаем json, добавляем новый жанр в бд"""
        model = self.model
        genre = model(**data)
        with db.session.begin():
            db.session.add(genre)

    def put_genre(self, uid: int, data: dict):
        """Обновляет жанр"""
        model = self.model
        genre = model.query.filter(model.id == uid).one()

        if "name" in data:
            genre.name = data.get("name")

        db.session.add(genre)
        db.session.commit()

    def get_genre_by_id(self, uid: int) -> dict:
        """Получаем жанр по id либо ошибка в str"""
        model = self.model
        schema = self.schema
        try:
            genre = model.query.filter(model.id == uid).one()
            return schema().dump(genre)
        except Exception as error:
            return str(error)

    def delete_genre(self, uid: int):
        """Удаляем жанр по id"""
        model = self.model
        genre = model.query.filter(model.id == uid).one()
        db.session.delete(genre)
        db.session.commit()
