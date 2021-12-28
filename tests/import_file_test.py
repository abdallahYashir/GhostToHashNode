import json
import unittest
from pprint import pprint

from process.importing import Importing
from process.transform import Transform


class ImportFileTests(unittest.TestCase):
    def test_valid_file(self):
        file_content = Importing('../test_data/valid.json')
        file_content.read_file()

        post = Transform(file_content.data)
        post.get_list_of_posts()
        self.assertEqual(len(post.posts), 1)

        is_valid = file_content.is_file_valid()
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.main()