import unittest
import sys

sys.path.append("src")

from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link


class Test_split_nodes(unittest.TestCase):
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_start_end(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_image_text_around(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and more text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and more text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_mixed(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and a link [link](https://google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and a link [link](https://google.com)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_only(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_no_image(self):
        node = TextNode(
            "This is text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_link_no_link(self):
        node = TextNode(
            "This is text",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_image_only(self):
        nodes = [TextNode("![My image](/images/my_image.png)", TextType.TEXT)]
        self.assertListEqual(
            split_nodes_image(nodes),
            [
                TextNode("My image", TextType.IMAGE, "/images/my_image.png"),
            ],
        )

    def test_split_image_multiple_images(self):
        nodes = [
            TextNode(
                "![First image](/images/first_image.png) and ![Second image](/images/second_image.png) and one more ![Third image](/images/third_image.png)",
                TextType.TEXT,
            )
        ]
        self.assertListEqual(
            split_nodes_image(nodes),
            [
                TextNode("First image", TextType.IMAGE, "/images/first_image.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("Second image", TextType.IMAGE, "/images/second_image.png"),
                TextNode(" and one more ", TextType.TEXT),
                TextNode("Third image", TextType.IMAGE, "/images/third_image.png"),
            ],
        )

    def test_split_link_only(self):
        nodes = [TextNode("[Home](/)", TextType.TEXT)]
        self.assertListEqual(
            split_nodes_link(nodes),
            [
                TextNode("Home", TextType.LINK, "/"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
