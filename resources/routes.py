from .auth import SignupApi


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
