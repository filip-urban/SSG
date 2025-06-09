import unittest

from text_node_to_html_node import text_node_to_html_node
from textnode import TextNode, TextType


class Testtext_node_to_html_node(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.testlink.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props, {"href": "www.testlink.com"})

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "image/path")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props.get("src"), "image/path")
        self.assertEqual(html_node.props.get("alt"), "This is an image")


if __name__ == "__main__":
    unittest.main()
