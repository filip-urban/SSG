import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
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
        text = "This is a text node"
        text_type = TextType.BOLD
        node = TextNode(f"{text}", text_type)
        self.assertEqual(node.__repr__(), f"TextNode({text}, {text_type.value})")

    def test_repr2(self):
        text = "This is a text node"
        text_type = TextType.LINK
        node = TextNode(f"{text}", text_type)
        self.assertEqual(node.__repr__(), f"TextNode({text}, {text_type.value})")

    def test_repr3(self):
        text = "This is a text node"
        text_type = TextType.LINK
        link = "www.testlink.com"
        node = TextNode(f"{text}", text_type, f"{link}")
        self.assertEqual(
            node.__repr__(), f"TextNode({text}, {text_type.value}, {link})"
        )


if __name__ == "__main__":
    unittest.main()
