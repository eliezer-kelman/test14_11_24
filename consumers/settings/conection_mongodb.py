import os
from pymongo import MongoClient

client = MongoClient(os.environ['MONGO_DB_URL'])

db = client['monitoring_messages']
all_messages_collection = db['all_messages']

def get_all_messages_collection():
    return all_messages_collection