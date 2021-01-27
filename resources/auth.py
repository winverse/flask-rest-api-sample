import datetime
from flask_jwt_extended import create_access_token, set_access_cookies
from flask import request, jsonify, make_response
from flask_restful import Resource

from database.user import User


class SignupApi(Resource):
    def post(self):
        body = request.get_json()

        if body == None:
            return {"message": "BAD_REQUEST"}, 400

        username = body.get('username')
        check_exists = User.query.filter_by(username=username).first()

        if check_exists:
            return {"duplicated": True}, 409

        user = User(**body)
        user.save()

        return jsonify(user)


class LoginApi(Resource):
    def post(self):
        body = request.get_json()

        if body == None:
            return {"message": "BAD_REQUEST"}, 400

        username = body.get('username')
        password = body.get('password')

        if not username or not password:
            return {"message": "BAD_REQUEST"}, 400

        user = User.query.filter_by(username=username).first()
        authorize = user.check_password(password)

        if not authorize:
            return {"message": "Wrong password"}, 401

        expires = datetime.timedelta(days=7)
        access_token = create_access_token(
            identity=str(user.id), expires_delta=expires)

        resp = make_response({"token": access_token})

        set_access_cookies(resp, access_token)

        return resp
