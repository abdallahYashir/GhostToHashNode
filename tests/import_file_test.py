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

    @unittest.skip("Can't test invalid test format for the moment")
    def test_json_file_format(self):
        # file_content = Importing('../test_data/sample.pdf')
        # file_content.read_file()
        self.assertRaises(Exception, "Invalid file format", Importing('../test_data/sample.pdf'))
        # self.assertRaises(Exception, "Invalid file format", file_content.read_file)

    def test_empty_file(self):
        file_content = Importing('../test_data/empty_file.json')
        file_content.read_file()
        self.assertRaises(Exception, "File is empty")

    def test_html_to_markdown(self):
        file = open('../test_data/html_markdown_data.json')
        content = json.load(file)
        # TODO: replace file reading with os.path.dirname(__file__)
        simple_post = content["simple_post"]
        html = simple_post["html"]
        markdown = simple_post["markdown"]
        self.assertEqual(Importing.convert_html_to_markdown(html), markdown)


if __name__ == '__main__':
    unittest.main()
