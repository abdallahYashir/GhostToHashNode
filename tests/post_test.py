import unittest
from collections import namedtuple
from pprint import pprint

from process.importing import Importing
from process.post import Post


def setup():
    file_content = Importing('../test_data/valid.json')
    file_content.read_file()
    post = Post(file_content.data)
    return post.get_list_of_posts()


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


if __name__ == '__main__':
    unittest.main()
