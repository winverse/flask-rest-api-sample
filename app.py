import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from database.db import db

from resources.routes import initialize_routes
DB_url = os.getenv('DATABASE_URI')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


migrate = Migrate(app, db)
db.app = app

db.init_app(app)

api = Api(app)

initialize_routes(api)
