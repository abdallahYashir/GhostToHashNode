from pprint import pprint

import markdownify

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
        return filtered_posts

    @staticmethod
    def dict_to_object(posts):
        list_ghost_posts = []
        if len(posts) > 0:
            for post in posts:
                new_ghost_post = Ghost(post['id'], post['title'], post['slug'], post['html'], post['plaintext'],
                                       post['status'], post['visibility'], post['feature_image'], post['published_at'],
                                       post['custom_excerpt'])
                list_ghost_posts.append(new_ghost_post)
        return list_ghost_posts

    def generate_front_matter(self, title, date, slug, image):
        # A better way is, with named parameters and .format():
        # https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
        fm = (
            '---'
            '\n'
            f'title: "{title}"'
            '\n\n'
            f'date: "{date}"'
            '\n\n'
            f'slug: "{slug}"'
            '\n\n'
            f'image: "{image}"'
            '\n\n'
            '---'
            '\n'
        )
        return fm

    def convert_html_to_markdown(self, html):
        return markdownify.markdownify(html)

    def generate_file(self, title, date, slug, image, html):
        fm = self.generate_front_matter(title, date, slug, image)
        content = self.convert_html_to_markdown(html)
        return fm + "\n\n" + content

    def is_ghost_valid(self, post):
        return False
