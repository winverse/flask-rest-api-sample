from flask_restful import Resource


class SignupApi(Resource):
    def post(self):
        return 'hello'
