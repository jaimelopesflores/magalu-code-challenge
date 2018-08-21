from flask import Flask
from flask_pymongo import PyMongo
from app.employee.controller import get_employee
from app.util.json import Encoder
from app.config import get_env

app = Flask(__name__)

# config
app.config['MONGO_URI'] = get_env('MONGO_URI')
app.json_encoder = Encoder

mongo = PyMongo(app)

app.register_blueprint(get_employee(mongo))
