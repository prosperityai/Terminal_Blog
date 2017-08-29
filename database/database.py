import pymongo

class Database(object):
  URI = 'mongodb://127.0.0.1:2701'
  DATABASE = None

  @staticmethond
  def initialize():
    client = pymongo.MongoClient(Database.URI)
    Database.DATABASE = client['prosperity']

  @staticmethond
  def insert(collection,data):
    Database.DATABASE[collection].insert(data)

  @staticmethond
  def find(collection,data):
    return Database.DATABASE[collection].find(query)

  @staticmethond
  def find_one(collection,query):
    return Database.DATABASE[collection].find_one(query)





