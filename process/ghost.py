class Ghost:
    def __init__(self, title, slug, html, plaintext, feature_image, published_at):
        self.title = title
        self.slug = slug
        self.html = html
        self.plaintext = plaintext
        self.feature_image = feature_image
        self.published_at = published_at

    def convert_html_markdown(self):
        self.html = ""
