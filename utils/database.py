from pymongo import MongoClient
from utils.exchange import create_exchange_data
from utils.config import get_dbinfo


class MongoController:
    def __init__(self, dbinfo_file, collections):
        dbinfo = get_dbinfo(dbinfo_file)
        self.connect(
            dbinfo["host"],
            dbinfo["port"],
            dbinfo["dbname"],
            collections
        )

    def connect(self, host, port, dbname, collections):
        self.client = MongoClient(host, port)
        self.set_dbname(dbname)
        self.set_collections(collections)

    def set_dbname(self, dbname):
        self.db = self.client[dbname]

    def set_collections(self, collections):
        self.collections = self.db[collections]

    def find_one(self, data):
        return self.collections.find_one(data)

    def insert_one(self, data):
        self.collections.insert_one(data)

    def update_one(self, search_data, data):
        self.collections.update_one(search_data, data)

    def get_exchange(self):
        return self.find_one({"name": "exchange"})

    def update_exchange(self, authkey):
        data = create_exchange_data(authkey)
        if data:
            if not self.find_one({"name": "exchange"}):
                self.insert_one(data)
            else:
                self.update_one({"name": "exchange"}, {"$set": data})
