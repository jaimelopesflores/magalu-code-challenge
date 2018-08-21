from flask import abort, Blueprint, request
from app.employee.model import Employee as EmployeeModel
def get_employee(mongo):

    model = EmployeeModel(mongo)
    employee = Blueprint('employee', __name__, url_prefix='/employee')

    @employee.route('/', defaults={'id': None})
    @employee.route('/<int:id>')
    def get(id):
        if id is None:
            return model.get_all()
        else:
            return model.get_by_id(id)

    @employee.route('/', methods=['POST'])
    def post():
        return model.create()

    @employee.route('/<int:id>', methods=['PUT'])
    def put(id):
        return model.update(id)

    @employee.route('/<int:id>', methods=['DELETE'])
    def delete(id):
       return model.remove(id)

    return employee
