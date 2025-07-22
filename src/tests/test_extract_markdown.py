import unittest
import sys
import os


sys.path.append("src")

from extract_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    extract_title,
)


class Testextract_markdown(unittest.TestCase):

    def test_extract_markdown_images_image_only(self):
        matches = extract_markdown_images("![My image](/images/my_image.png)")
        self.assertListEqual(matches, [("My image", "/images/my_image.png")])

    def test_extract_markdown_links_link_only(self):
        matches = extract_markdown_links("[My link](www.mywebsite.com/my_link)")
        self.assertListEqual(matches, [("My link", "www.mywebsite.com/my_link")])

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![some image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("some image", "https://i.imgur.com/zjjcJKZ.png")], matches
        )

    def test_extract_markdown_image_and_link(self):
        text = "This is a text with a link [link](www.google.com) and with an image ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches_link = extract_markdown_links(text)
        matches_image = extract_markdown_images(text)
        self.assertListEqual([("link", "www.google.com")], matches_link)
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches_image
        )

    def test_extract_markdown_link(self):
        matches = extract_markdown_links(
            "This is a text with a link [link](www.google.com) and with an another link [different link](www.youtube.com))"
        )
        self.assertListEqual(
            [("link", "www.google.com"), ("different link", "www.youtube.com")], matches
        )

    def test_extract_title(self):
        md_file = "test_extract_title.md"
        markdown = """#   important heading   
some text
more text"""
        with open(md_file, "w+") as fh:
            fh.write(markdown)

        self.assertEqual("important heading", extract_title(md_file))
        os.remove(md_file)

    def test_extract_title_exception(self):
        md_file = "test_extract_title.md"
        markdown = """## heading   
some text
more text"""
        with open(md_file, "w+") as fh:
            fh.write(markdown)

        with self.assertRaises(Exception):
            extract_title(md_file)

        os.remove(md_file)


if __name__ == "__main__":
    unittest.main()
