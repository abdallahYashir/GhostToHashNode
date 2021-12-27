import json
import unittest
from pprint import pprint

from process.importing import Importing
from process.post import Post


class ImportFileTests(unittest.TestCase):
    def test_valid_file(self):
        file_content = Importing('../test_data/valid.json')
        file_content.read_file()
        post = Post(file_content.data)
        posts = post.get_list_of_posts()
        self.assertEqual(len(post.posts), 1)


if __name__ == '__main__':
    unittest.main()
