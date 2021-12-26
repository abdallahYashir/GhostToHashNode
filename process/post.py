from pprint import pprint

from process.document import Datum, DB


class Post:
    def __init__(self, data):
        self.data = data
        self.posts = []

    def get_list_of_posts(self):
        # should return list of posts
        # doc = Datum(**self.data)
        # db = list(self.data.keys())[0]
        db = self.data["db"]
        self.posts = list(db)[0]["data"]["posts"]
        return self.posts

    def filter_posts(self, number, status):
        # from itertools import ifilter
        # for elem in ifilter(lambda x: x['type'] in keyValList, exampleSet):
        #     print
        #     elem
        filtered_posts = [post for post in self.posts if post['status'] == 'published']
        pprint(filtered_posts)
        return None
