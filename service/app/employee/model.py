
class Employee:

    def __init__(self, mongo):
        self.mongo = mongo

    def get_all(self):
        return 'all'

    def get_by_id(self, id):
        return 'get: ' + str(id)

    def create(self):
        return 'create'

    def update(self, id):
        return 'update: ' + str(id)

    def remove(self, id):
        return 'remove: ' + str(id)
