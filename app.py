
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)

app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['JWT_SECRET_KEY'] = 'flask-rest-api-example'

api = Api(app)
jwt = JWTManager(app)

initialize_routes(api)
initialize_db(app)
