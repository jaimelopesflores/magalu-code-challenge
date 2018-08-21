from flask import abort, Blueprint, jsonify, request
from app.employee.model import Employee as EmployeeModel

def get_employee(mongo):

    model = EmployeeModel(mongo)
    employee = Blueprint('employee', __name__, url_prefix='/employee')

    @employee.route('/')
    def get():
        return jsonify(model.get_all())

    @employee.route('/<objectid>')
    def get_one(objectid):
        entity = model.get_by_id(objectid)
        return abort(404) if entity is None else jsonify(entity)

    @employee.route('/', methods=['POST'])
    def post():
        id = model.create(request.json)
        return get_one(id)

    @employee.route('/<id>', methods=['PUT'])
    def put(id):
        model.update(id, request.json)
        return get_one(id)

    @employee.route('/<id>', methods=['DELETE'])
    def delete(id):
        return jsonify(model.remove(id))

    return employee
