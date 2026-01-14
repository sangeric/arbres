from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = "mongodb://localhost:27017/"
    client = MongoClient(CONNECTION_STRING)
    db = client["arbres_db"]   # nom de la base
    return db


"""
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "arbres_db"
COLLECTION_NAME = "arbres"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]
"""


