import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=html_props)
        self.assertEqual(
            node.props_to_html(), 'href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html2(self):
        html_props = {
            "href": "https://www.google.com",
        }
        node = HTMLNode(props=html_props)
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')

    def test_props_to_html3(self):
        html_props = {}
        node = HTMLNode(props=html_props)
        self.assertEqual(node.props_to_html(), "")


if __name__ == "__main__":
    unittest.main()
