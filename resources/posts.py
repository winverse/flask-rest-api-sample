from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity


class Create(Resource):
    @jwt_required
    def post(self):
        user = get_jwt_identity()
        print(user)
        return 'create'


class List(Resource):
    def get(self):
        return 'list'


class Read(Resource):
    def get(self, post_id):
        return 'read'


class Remove(Resource):
    def delete(self, post_id):
        return 'remove'
