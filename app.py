
from flask import Flask
from flask_restful import Api

from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

initialize_routes(api)
initialize_db(app)
