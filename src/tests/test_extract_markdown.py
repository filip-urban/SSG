import unittest
import sys

sys.path.append("src")

from extract_markdown import extract_markdown_images, extract_markdown_links


class Testextract_markdown(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
