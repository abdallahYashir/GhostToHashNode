class Ghost:
    def __init__(self, title, slug, html, plaintext, status, visibility, feature_image, published_at, custom_excerpt):
        self.id = id
        self.title = title
        self.slug = slug
        self.html = html
        self.plaintext = plaintext
        self.status = status
        self.visibility = visibility
        self.feature_image = feature_image
        self.published_at = published_at
        self.custom_excerpt = custom_excerpt

    def convert_html_markdown(self):
        self.html = ""
