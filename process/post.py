from pprint import pprint


class Post:
    def __init__(self, data):
        self.data = data
        self.posts = []

    def get_list_of_posts(self):
        db = self.data["db"]
        self.posts = list(db)[0]["data"]["posts"]
        return self.posts

    def filter_posts(self, number, status):
        filtered_posts = [post for post in self.posts if post['status'] == 'published']
        filtered_posts = filtered_posts[-number:]
        pprint(filtered_posts)
        return filtered_posts

    def is_ghost_valid(self, post):
        return False
