from flask import request, jsonify
from flask_restful import Resource

from database.user import User


class SignupApi(Resource):
    def post(self):
        body = request.get_json()

        username = body['username']
        check_exists = User.query.filter_by(username=username).first()

        if check_exists:
            return {"duplicated": True}, 409

        user = User(**body)
        user.save()

        return jsonify(user)
