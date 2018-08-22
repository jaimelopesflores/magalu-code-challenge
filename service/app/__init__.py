from flask import Flask
from flask_pymongo import PyMongo
from app.employee.controller import get_employee
from app.util.json import Encoder
from app.util.mongo import Transform
from app.config import get_env

app = Flask(__name__)
app.config['MONGO_URI'] = get_env('MONGO_URI')
app.json_encoder = Encoder

mongo = PyMongo(app)
mongo.db.add_son_manipulator(Transform())

app.register_blueprint(get_employee(mongo))
