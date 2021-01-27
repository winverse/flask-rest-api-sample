from .auth import SignupApi, LoginApi
from .posts import Create, Remove, List, Read


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')

    api.add_resource(Create, '/api/posts')
    api.add_resource(Read, '/api/posts/<post_id>')
    api.add_resource(List, '/api/posts')
    api.add_resource(Remove, '/api/posts/<post_id>')
