import  pymongo
#testing pymongo
url="mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(url)
database = client['prosperity']
collection = database['students']

students = collection.find({})
for student in students:
  print(student)
