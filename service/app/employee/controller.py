from flask import abort, Blueprint, jsonify, request
from jsonschema import validate, ValidationError
from app.employee.model import Employee as EmployeeModel
from app.employee.schema import schema

def get_employee(mongo):

    model = EmployeeModel(mongo)
    employee = Blueprint('employee', __name__, url_prefix='/employee')

    @employee.route('/')
    def get():
        return jsonify(model.get_all())

    @employee.route('/<objectid>')
    def get_one(objectid):
        entity = model.get_by_id(objectid)
        return abort(404, 'Employee not found') if entity is None else jsonify(entity)

    @employee.route('/', methods=['POST'])
    def post():
        try:
            validate(request.json, schema)
            id = model.create(request.json)
            return get_one(id)
        except ValidationError:
            abort(400, 'Schema is not valid!')

    @employee.route('/<id>', methods=['PUT'])
    def put(id):
        try:
            validate(request.json, schema)
            model.update(id, request.json)
            return get_one(id)
        except ValidationError:
            abort(400, 'Schema is not valid!')

    @employee.route('/<id>', methods=['DELETE'])
    def delete(id):
        return jsonify(model.remove(id))

    return employee
