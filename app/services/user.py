from app.dao.user_dao import UserDAO


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one_by_id(self, uid: int) -> dict:
        return self.dao.get_one_by_id(uid)

    def add_new_user(self, data: dict):
        self.dao.add_new_user(data)

    def update_user(self, uid: int, data: dict):
        user = self.get_one_by_id(uid)
        if "username" in data:
            user.username = data.get("username")
        if "password" in data:
            user.username = data.get("password")
        if "role" in data:
            user.username = data.get("role")

        self.dao.update_user(user)

    def delete_user(self, uid: int):
        self.dao.delete_user(uid)
