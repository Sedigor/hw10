from pymongo import MongoClient


# mongo db connection

def get_mongodb():
    client = MongoClient('mongodb+srv://sisem:6ykeaurkl3dT5OLs@ihorlearn.zjsspul.mongodb.net/db_hw_8?retryWrites=true&w=majority')
    db = client['db_hw_8']
    return db