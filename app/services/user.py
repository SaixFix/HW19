import hashlib

from app.dao.user_dao import UserDAO
from app.config import Config
from app.helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one_by_id(self, uid: int) -> dict:
        return self.dao.get_one_by_id(uid)

    def get_one_by_username(self, username: str) -> dict:
        return self.dao.get_one_by_username(username)

    def add_new_user(self, data: dict):
        data["password"] = self.generated_password(data["password"])
        self.dao.add_new_user(data)

    def update_user(self, uid: int, data: dict):
        user = self.get_one_by_id(uid)
        user["password"] = self.generated_password(data["password"])
        if "username" in data:
            user.username = data.get("username")
        if "password" in data:
            user.username = data.get("password")
        if "role" in data:
            user.username = data.get("role")

        self.dao.update_user(user)

    def delete_user(self, uid: int):
        self.dao.delete_user(uid)

    def generated_password(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")
