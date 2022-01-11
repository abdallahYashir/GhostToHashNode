import json
import mimetypes
import os.path
import pathlib
from pathlib import Path
from pprint import pprint
import markdownify


def check_valid_file_format(path):
    guess = mimetypes.guess_type(path)
    json_type = 'application/json'
    if str(guess[0]) != json_type:
        raise Exception("Invalid file format")


class Importing:
    def __init__(self, file_name):
        self.data = None
        self.file_content = None
        self.file_name = self.get_file_path(file_name)
        self.read_file()

    def get_file_path(self, file_name):
        return Path(file_name).resolve()

    def read_file(self):
        check_valid_file_format(self.file_name)
        self.file_content = open(self.file_name, encoding="utf8")
        self.data = json.load(self.file_content)
        if self.data is None:
            raise Exception("Empty JSON File")

    def is_file_valid(self):
        valid = True
        if len(list(self.data["db"])) == 0:
            valid = False
        else:
            if "data" in list(self.data["db"])[0]:
                valid = True
                if "posts" in list(self.data["db"])[0]["data"]:
                    valid = True
                else:
                    valid = False
            else:
                valid = False

        return valid
