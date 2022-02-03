import codecs
import os.path
import shutil
import zipfile
from pprint import pprint
from random import randrange

from slugify import slugify

from process import box
from process.importing import Importing
from process.transform import Transform
from pathlib import Path


def main():
    # TODO: only take the file name -> let Importing class do the rest
    file = Importing("abdallah-yashir-blog.ghost.json")
    transform_file = Transform(file.data)
    transform_file.get_list_of_posts()
    my_posts = transform_file.filter_posts(10, 'published')
    print(len(my_posts))
    # pprint(my_posts[0])
    ghost_posts = Transform.dict_to_object(my_posts)
    pprint(ghost_posts[0].title)
    single_post = ghost_posts[0]
    # Convert one file
    sample_file = transform_file.generate_file(single_post.title, single_post.published_at, single_post.slug,
                                               single_post.feature_image,
                                               single_post.html)
    # pprint(sample_file.strip())
    folder_name = "posts"
    box.sync_folder(folder_name)

    for post in ghost_posts[:2]:
        p = transform_file.generate_file(post.title, post.published_at, post.slug,
                                         post.feature_image,
                                         post.html)
        # file_title = post.title.replace(' ', '-')
        file_title = slugify(post.title + "-" + post.published_at)
        filepath = Path(f"{folder_name}/{file_title}.md")
        filepath.parent.mkdir(parents=True, exist_ok=True)

        with filepath.open("w", encoding="utf-8") as f:
            f.write(p)

    # TODO: zip the posts folder
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    output_filename = 'posts'
    shutil.make_archive(output_filename, 'zip', os.path.join(ROOT_DIR, folder_name))

    ''' ENHANCEMENT: check if zip folder is correct '''


    exit(0)

    with open("output.md", "w", encoding="utf-8") as text_file:
        # text_file.write(codecs.BOM_UTF8)
        text_file.write("%s" % sample_file)
        # convert sample file to a zip

    # file_path = Path("output.md").resolve()
    # zipfile.ZipFile('posts.zip', mode='w').write("output.md")
    # zipfile.ZipFile('posts.zip', mode='w').write(file_path)
    # NOTE: this code works
    # TODO: get last 10 posts
    # TODO: create a directory call posts
    # TODO: write files in posts
    # TODO: zip file the whole posts folder
    # TODO: delete the posts folder
    with zipfile.ZipFile('posts.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
        zip.write("output.md")


if __name__ == "__main__":
    main()
