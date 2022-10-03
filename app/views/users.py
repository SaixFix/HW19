from flask import request
from flask_restx import Namespace, Resource

from app.container import user_service
from app.dao.models.user import UserSchema
from app.dao.user_dao import UserDAO

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        """Показывает всех юзеров"""
        users = user_service.get_all()
        return users_schema.dump(users), 200

    def post(self):
        """Добавление нового юзера"""
        req_json = request.json
        user_service.add_new_user(req_json)
        return f" Пользователь {req_json['username']} добавлен", 201

@user_ns.route('/<int:uid>')
class UserWiew(Resource):
    def put(self, uid):
        """Обновление юзера по id"""
        req_json = request.json
        user_service.update_user(uid, req_json)
        return f" Пользователь {uid} обновлен", 201
