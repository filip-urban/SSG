from split_nodes import split_nodes_image, split_nodes_link, split_nodes_delimiter
from textnode import TextNode, TextType


def text_to_textnodes(text):
    split_nodes = split_nodes_link(split_nodes_image([TextNode(text, TextType.TEXT)]))
    split_nodes = split_nodes_delimiter(split_nodes, "**", TextType.BOLD)
    split_nodes = split_nodes_delimiter(split_nodes, "_", TextType.ITALIC)
    split_nodes = split_nodes_delimiter(split_nodes, "`", TextType.CODE)
    return split_nodes
