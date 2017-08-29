import  pymongo
#testing pymongo
url="mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(url)
database = client['prosperity']
collection = database['students']

students = [student for student in collection.find({})]
print(students)
