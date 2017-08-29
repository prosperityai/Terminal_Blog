class Post(object):
  """docstring for Post"""
  def __init__(self, blog_id, title,content,author,idt,date):
     self.blog_id = blog_id
    self.title = title
    self.content = content
    self.author = author
    self.idt = idt
    self.created_date = date

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
 def from_mongo(idt):
   return Database.find_one(collections='posts',query ={'idt':idt})

   @staticmethod
 def from_mongo(idt):
   return [post for post in Database.find(collections='posts',query ={'blog_id':idt})]
