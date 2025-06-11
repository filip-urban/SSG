import unittest
import sys

sys.path.append("src")

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class Testsplit_nodes_delimiter(unittest.TestCase):

    def test_inline_only(self):
        node = TextNode("**bolded text**", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("bolded text", TextType.BOLD),
            ],
        )

    def test_inline_left(self):
        node = TextNode("**Bolded text** and normal text", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("Bolded text", TextType.BOLD),
                TextNode(" and normal text", TextType.TEXT),
            ],
        )

    def test_inline_middle(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_inline_right(self):
        node = TextNode("This is text with a `code block`", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
            ],
        )

    def test_inline_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
