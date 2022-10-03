from app.dao.models.user import User


class UserDAO:

    def __init__(self, session):
        """Получает модель и схему"""
        self.session = session

    def get_all(self):
        """Получаем всех пользователей"""
        return self.session.query(User).all()

    def get_one_by_id(self, uid: int) -> dict:
        """Получаем юзера по id"""
        return self.session.query(User).get(uid)

    def add_new_user(self, data: dict):
        """Получаем словарь, добавляем юзера"""
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update_user(self, user: dict):
        """Обновляем данные пользователя по id"""
        self.session.add(user)
        self.session.commit()

        return User


