import json
from pprint import pprint


class Importing:
    def __init__(self, path):
        self.data = None
        self.file_content = None
        self.path = path
        self.read_file()

    def read_file(self):
        self.file_content = open(self.path)
        self.data = json.load(self.file_content)

    def is_file_valid(self):
        # should contain dd
        # db[0] should be a list with properties data
        # data should contain at least one post property
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
