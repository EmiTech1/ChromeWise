# import pymongo

# class Connection:
#     def __init__(self):
#         self.client = pymongo.MongoClient(
#             "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.4")
#         self.db = self.client['monica']
#         self.collection = self.db['user']






import pymongo
import mongoengine

class Connection:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.4")
        self.db = self.client['monica']
        self.collection = self.db['user']
        
        mongoengine.connect(db='monica', host='127.0.0.1', port=27017)


#     def fetch_data(self):

#         data = self.collection.find()

#         for document in data:
#             print(document)


# connection = Connection()

# connection.fetch_data()
