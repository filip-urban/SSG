import unittest
import sys

sys.path.append("src")

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(
            node.__repr__(),
            f"TextNode(This is a text node, {TextType.BOLD.value})",
        )

    def test_repr2(self):
        node = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(
            node.__repr__(),
            f"TextNode(This is a text node, {TextType.LINK.value})",
        )

    def test_repr3(self):
        node = TextNode("This is a text node", TextType.LINK, "www.testlink.com")
        self.assertEqual(
            node.__repr__(),
            f"TextNode(This is a text node, {TextType.LINK.value}, www.testlink.com)",
        )


if __name__ == "__main__":
    unittest.main()
