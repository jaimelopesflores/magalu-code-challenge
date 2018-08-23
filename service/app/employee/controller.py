from flask import abort, Blueprint, jsonify, request
from jsonschema import validate, ValidationError
from app.employee.model import Employee as EmployeeModel
from app.employee.schema import schema

def get_employee(mongo):

    model = EmployeeModel(mongo)
    employee = Blueprint('employee', __name__, url_prefix='/employee')

    @employee.route('/')
    @employee.route('')
    def get():
        return jsonify(model.get_all())

    @employee.route('/<id>/')
    @employee.route('/<id>')
    def get_one(id):
        entity = model.get_by_id(id)
        print('Get by id %s' % id)
        return abort(404, 'Employee not found') if entity is None else jsonify(entity)

    @employee.route('/', methods=['POST'])
    @employee.route('', methods=['POST'])
    def post():
        try:
            validate(request.json, schema)
            id = model.create(request.json)
            print('Created id %s' % id)
            return get_one(id)
        except ValidationError:
            abort(400, 'Schema is not valid!')

    @employee.route('/<id>/', methods=['PUT'])
    @employee.route('/<id>', methods=['PUT'])
    def put(id):
        try:
            validate(request.json, schema)
            model.update(id, request.json)
            print('Updated id %s' % id)
            return get_one(id)
        except ValidationError:
            abort(400, 'Schema is not valid!')

    @employee.route('/<id>/', methods=['DELETE'])
    @employee.route('/<id>', methods=['DELETE'])
    def delete(id):
        print('Deleted id %s' % id)
        return jsonify(model.remove(id))

    return employee
