from pprint import pprint

from process.ghost import Ghost


class Transform:
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

    @staticmethod
    def dict_to_object(posts):
        list_ghost_posts = []
        if len(posts) > 0:
            for post in posts:
                new_ghost_post = Ghost(post['id'], post['title'], post['slug'], post['html'], post['plaintext'], post['status'], post['visibility'], post['feature_image'], post['published_at'], post['custom_excerpt'])
                list_ghost_posts.append(new_ghost_post)
        return list_ghost_posts

    def is_ghost_valid(self, post):
        return False
