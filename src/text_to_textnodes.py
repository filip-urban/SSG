from split_nodes import split_nodes_image, split_nodes_link
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


def text_to_textnodes(text):
    links_and_images = split_nodes_link(
        split_nodes_image([TextNode(text, TextType.TEXT)])
    )
    links_and_images_and_bold = split_nodes_delimiter(
        links_and_images, "**", TextType.BOLD
    )
    links_and_images_and_emphasis = split_nodes_delimiter(
        links_and_images_and_bold, "_", TextType.ITALIC
    )
    links_and_images_emphasis_and_code = split_nodes_delimiter(
        links_and_images_and_emphasis, "`", TextType.CODE
    )
    return links_and_images_emphasis_and_code
