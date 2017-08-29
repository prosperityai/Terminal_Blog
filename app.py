from database import Database
from models.blog import Blog

Database.initialize()


post = Post(blog_id ="123":,
            title = 'Another terminal blog',
            content = "Some contents",
            author = "Prosperity King"
  )
blog.new_post()

post.save_to_mongo()

from_database = Blog.from_mongo()

print(blog.getposts())