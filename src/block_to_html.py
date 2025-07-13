import re

from markdown_to_blocks import markdown_to_blocks
from markdown_to_blocks import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from htmlnode import ParentNode
from textnode import TextNode, TextType


def create_child_nodes(text):
    text_nodes = text_to_textnodes(
        text.replace("\n", " ")
    )  # newlines should convert to spaces in MD
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes


def create_list(text, list_chars):
    html_nodes = []
    for line in text.split("\n"):
        if not line:
            continue
        list_node = ParentNode("li", [])
        text_nodes = text_to_textnodes(line[list_chars:].replace("\n", " "))
        for text_node in text_nodes:
            list_node.children.append(text_node_to_html_node(text_node))
        html_nodes.append(list_node)
    return html_nodes


def create_blockquote(block):
    text_list = [line[2:] for line in block.split("\n")]
    return create_child_nodes(" ".join(text_list))


def create_html_nodes_from_block(block_type, block):
    U_LIST_BULLET_SIZE = 2
    O_LIST_BULLET_SIZE = 3
    match block_type:
        case BlockType.HEADING:
            heading_level = 1
            for char in block[1:]:
                if char != "#" or heading_level == 6:
                    break
                heading_level += 1
            return ParentNode(
                f"h{heading_level}",
                create_child_nodes(block[heading_level + 1 :]),
            )
        case BlockType.PARAGRAPH:
            return ParentNode("p", create_child_nodes(block))
        case BlockType.CODE:
            text_node = TextNode(block[4:-3], TextType.CODE)
            return ParentNode("pre", [text_node_to_html_node(text_node)])
        case BlockType.QUOTE:
            return ParentNode("blockquote", create_blockquote(block))
        case BlockType.UNORDERED_LIST:
            return ParentNode("ul", create_list(block, U_LIST_BULLET_SIZE))
        case BlockType.ORDERED_LIST:
            return ParentNode("ol", create_list(block, O_LIST_BULLET_SIZE))


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root_node = ParentNode("div", [])
    for block in blocks:
        type = block_to_block_type(block)
        root_node.children.append(create_html_nodes_from_block(type, block))
    return root_node
