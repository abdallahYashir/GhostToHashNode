from process.importing import Importing
from process.post import Post

file = Importing("../abdallah-yashir-blog.ghost.2021-12-26.json")
post = Post(file.data)

post.get_list_of_posts()
post.filter_posts(10, 'published')
