import unittest
from collections import namedtuple
from pprint import pprint

from process.importing import Importing
from process.transform import Transform

def setup():
    file_content = Importing('../test_data/valid.json')
    file_content.read_file()
    transform = Transform(file_content.data)
    return transform.get_list_of_posts()


class MyTestCase(unittest.TestCase):

    def test_post_should_not_be_empty(self):
        posts = setup()
        self.assertEqual(len(posts), 1)

    def test_ghost_should_contain_properties(self):
        posts = setup()
        first_post = posts[0]

        if all(key in first_post for key in ("id", "title", "slug", "html", "plaintext", "status", "visibility", "feature_image", "published_at", "custom_excerpt")):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_should_transform_to_ghost_object(self):
        posts = setup()
        ghost_posts = Transform.dict_to_object(posts)
        self.assertEqual(len(ghost_posts), 1)
        first_ghost_post = ghost_posts[0]
        self.assertEqual(first_ghost_post.id, "5c32fc7fc8b30b0807136770")
        self.assertEqual(first_ghost_post.title, "Writing to Share & Teach")

if __name__ == '__main__':
    unittest.main()
