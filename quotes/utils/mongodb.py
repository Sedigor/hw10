import configparser
from pymongo import MongoClient


config = configparser.ConfigParser()
config.read('utils/config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

def get_mongodb():
    client = MongoClient(f'mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority')
    db = client[db_name]
    return db

