from flask import Flask
from app.employee.controller import employee as employee_module

app = Flask(__name__)

# config
app.config.from_object('config')

app.register_blueprint(employee_module)
