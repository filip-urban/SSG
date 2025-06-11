import unittest
import sys

sys.path.append("src")

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com" target="_blank"',
        )

    def test_props_to_html2(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
            }
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.google.com"',
        )

    def test_props_to_html3(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, This is a paragraph, None, {'class': 'primary'})",
        )

    def test_values(self):
        node = HTMLNode(
            "b",
            "Bold text",
        )
        self.assertEqual(
            node.tag,
            "b",
        )
        self.assertEqual(
            node.value,
            "Bold text",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )


if __name__ == "__main__":
    unittest.main()
