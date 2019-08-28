import pymongo
from pymongo import MongoClient
from pymongo import ASCENDING


class Database(object):
    def __init__(self, address, port, database):
        self.conn = MongoClient(host=address, port=port)
        self.db = self.conn[database]

    def get_state(self):
        return self.conn is not None and self.db is not None

    def insert_one(self, collection, data):
        if self.get_state():
            ret = self.db[collection].insert_one(data)
            return ret.inserted_id
        else:
            return ""

    def insert_many(self, collection, data):
        if self.get_state():
            ret = self.db[collection].insert_many(data)
            return ret.inserted_id
        else:
            return ""

    def update(self, collection, data):
        # data format:
        # {key:[old_data,new_data]}
        data_filter = {}
        data_revised = {}
        for key in data.keys():
            data_filter[key] = data[key][0]
            data_revised[key] = data[key][1]
        if self.get_state():
            return self.db[collection].update_many(data_filter, {"$set": data_revised}).modified_count
        return 0

    def get_collection(self, name):
        return self.db[name]

    def find(self, col, condition, column=None):
        if self.get_state():
            if column is None:
                return self.db[col].find(condition)
            else:
                return self.db[col].find(condition, column)
        else:
            return None

    def delete(self, col, condition):
        if self.get_state():
            return self.db[col].delete_many(filter=condition).deleted_count
        return 0


# client = MongoClient('localhost', 27017)
# db = client.school
# coll = db.students
# # coll.create_index([('name', ASCENDING)], unique=True)
# # coll.insert_one({'stuid': int(1001), 'name': 'xxx', 'gender': True})

if __name__ == "__main__":
    dataBase = Database("localhost", 27017, "school")
    coll = dataBase.get_collection("students")
    item = dataBase.find("students", {'stuid' : 1001})

    for student in item:
        print("学号:", student['stuid'])
