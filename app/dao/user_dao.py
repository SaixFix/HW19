from app.setup_db import db

class UserDAO:

    def __init__(self, model, schema):
        """Получает модель и схему"""
        self.model = model
        self.schema = schema

    def get_all(self):
        """Получаем всех пользователей"""
        users = self.model.querry.all()
        return self.schema(many=True).dump(users)

    def get_one_by_id(self, uid: int) -> dict:
        """Получаем юзера по id"""
        model = self.model
        schema = self.schema
        try:
            user = model.query.filtyer(model.id == uid).one()
            return schema().dump(user)
        except Exception as error:
            return str(error)

    def add_new_user(self, data: dict):
        """Получаем словарь, добавляем юзера"""
        model = self.model
        user = model(**data)
        with db.session.begin():
            db.session.add(user)

    def update_user(self, uid: int, data: dict):
        """Обновляем данные пользователя по id"""
        model = self.model
        user = model.query.filter(model.id == uid).one()

        if "username" in data:
            user.username = data.get("username")
        if "password" in data:
            user.username = data.get("password")
        if "role" in data:
            user.username = data.get("role")

        db.session.add(user)
        db.session.commit()


