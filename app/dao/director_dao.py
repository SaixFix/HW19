


class DirectorDAO:

    def __init__(self, session):
        """Получает модель и схему"""
        self.session = session

    def get_all(self) -> list[dict]:
        """Возвращает список всех данных"""
        genres = self.model.query.all()
        return self.schema(many=True).dump(genres)

    def add_director(self, data: dict):
        """Получаем json, добавляем нового режиссера в бд"""
        model = self.model
        genre = model(**data)
        with db.session.begin():
            db.session.add(genre)

    def put_director(self, uid: int, data: dict):
        """Обновляет режиссера"""
        model = self.model
        genre = model.query.filter(model.id == uid).one()

        if "name" in data:
            genre.name = data.get("name")

        db.session.add(genre)
        db.session.commit()

    def get_director_by_id(self, uid: int) -> dict:
        """Получаем режиссера по id либо ошибка в str"""
        model = self.model
        schema = self.schema
        try:
            genre = model.query.filter(model.id == uid).one()
            return schema().dump(genre)
        except Exception as error:
            return str(error)

    def delete_director(self, uid: int):
        """Удаляем режиссера по id"""
        model = self.model
        genre = model.query.filter(model.id == uid).one()
        db.session.delete(genre)
        db.session.commit()
