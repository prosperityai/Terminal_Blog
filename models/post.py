import uuid
from database import Database
import datetime
class Post(object):
  """docstring for Post"""
  def __init__(self, blog_id, title,content,author,date = datetime.datetime.utcnow(),id=None):
     self.blog_id = blog_id
    self.title = title
    self.content = content
    self.author = author
    self.created_date = date
    self.idt = uuid.uuid4().hexa if id is None else id


  def mongo_save(self):
    Database.insert(collections = 'posts',data = self.json)


  def json(self):
    return{
    'blog_id': self.blog_id
    'title': self.title
    'content': self.content
    'author' : self.author
    'idt' :self.idt
    'created_date': self.date
    }


  @staticmethod
 def from_mongo(id):
   return Database.find_one(collections='posts',query ={'id':id})

   @staticmethod
 def from_mongo(id):
   return [post for post in Database.find(collections='posts',query ={'blog_id':id})]
