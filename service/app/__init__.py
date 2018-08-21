from flask import Flask
from flask_pymongo import PyMongo
from app.employee.controller import get_employee

app = Flask(__name__)

# config
app.config.from_object('config')
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"

mongo = PyMongo(app)

app.register_blueprint(get_employee(mongo))
