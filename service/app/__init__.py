from flask import Flask
from flask_pymongo import PyMongo
from app.employee.controller import get_employee
from app.util.json import Encoder

app = Flask(__name__)

# config
app.config.from_object('config')
app.config["MONGO_URI"] = "mongodb://db:27017/magalu"
app.json_encoder = Encoder

mongo = PyMongo(app)

app.register_blueprint(get_employee(mongo))
