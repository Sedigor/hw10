import os

os.environ['db_name'] = 'mongodb'

var1 = os.getenv('db_name')
print(var1)

