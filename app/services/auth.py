import calendar
import datetime

import jwt
from flask_restx import abort

from app.helpers.constants import JWT_SECRET, JWT_ALGORITHM
from app.services.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_token(self, username, password):
        user = self.user_service.get_one_by_username(username)

        if user is None:
            raise abort(404)

        if not self.user_service.compare_passwords(user.password, password):
            abort(400)

        data = {
            "username": user.username,
            "role": user.role
        }

        #30 minut for access token

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        acceess_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        #130 days for refresh_token
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {
            "acceess_token": acceess_token,
            "refresh_token": refresh_token
        }

