from flask import abort, Blueprint, request
from app.employee.model import get_all, get_by_id, create, update, remove

employee = Blueprint('employee', __name__, url_prefix='/employee')

@employee.route('/', defaults={'id': None})
@employee.route('/<int:id>')
def get(id):
    if id is None:
        return get_all()
    else:
        return get_by_id(id)

@employee.route('/', methods=['POST'])
def post():
    return create()

@employee.route('/<int:id>', methods=['PUT'])
def put(id):
    return update(id)

@employee.route('/<int:id>', methods=['DELETE'])
def delete(id):
    return remove(id)
