from process.importing import Importing
from process.transform import Transform

file = Importing("../abdallah-yashir-blog.ghost.2021-12-26.json")
post = Transform(file.data)

post.get_list_of_posts()
my_posts = post.filter_posts(10, 'published')
print(len(my_posts))