from bson.objectid import ObjectId

class Employee:

    def __init__(self, mongo):
        self.mongo = mongo

    def get_all(self):
        cursor = self.mongo.db.employee.find()
        return list(cursor)

    def get_by_id(self, id):
        return self.mongo.db.employee.find_one({"_id": ObjectId(id)})

    def create(self, data):
        return self.mongo.db.employee.insert_one(data).inserted_id

    def update(self, id, data):
        return self.mongo.db.employee.find_one_and_update({'_id': ObjectId(id)}, {'$set': data})

    def remove(self, id):
        return self.mongo.db.employee.remove({"_id": ObjectId(id)})
