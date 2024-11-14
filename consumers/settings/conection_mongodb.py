import os
from pymongo import MongoClient

client = MongoClient('mongodb://172.24.255.254  :27017/')

def get_all_messages_collection():
    db = client['monitoring_messages']
    all_messages_collection = db['all_messages']
    return all_messages_collection
