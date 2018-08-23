from pymongo.son_manipulator import SONManipulator

class Transform(SONManipulator):
    def transform_outgoing(self, son, collection):
        return { key.replace('_', ''): value for key, value in son.items() }
