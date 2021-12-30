from pprint import pprint

from process.importing import Importing
from process.transform import Transform

file = Importing("../abdallah-yashir-blog.ghost.2021-12-26.json")
transform_file = Transform(file.data)

transform_file.get_list_of_posts()
my_posts = transform_file.filter_posts(10, 'published')
print(len(my_posts))
# pprint(my_posts[0])

ghost_posts = Transform.dict_to_object(my_posts)
pprint(ghost_posts[0].title)
single_post = ghost_posts[0]

# Convert one file
sample_file = transform_file.generate_file(single_post.title, single_post.published_at, single_post.slug, single_post.feature_image,
                                           single_post.html)

pprint(sample_file)
