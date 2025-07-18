import unittest
import sys

sys.path.append("src")

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Stuff")
        self.assertEqual(node.to_html(), "Stuff")


if __name__ == "__main__":
    unittest.main()
