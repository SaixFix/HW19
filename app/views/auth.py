from flask import request
from flask_restx import Namespace, Resource
from app.helpers.decorators import auth_required

auth_ns = Namespace("auth")


@auth_ns.route("/")
class AuthsView(Resource):
    def post(self):
        data = request.json

        username = data.get("username", None)
        password = data.get("password", None)

        if None in [username, password]:
            return "", 400

        token = auth_service.generate_tokens(username, password)
