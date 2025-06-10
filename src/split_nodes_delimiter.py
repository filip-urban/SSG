from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes_result.extend(node)
            continue
        split_nodes = node.text.split(delimiter)
        if len(split_nodes) < 2:
            nodes_result.extend(node)
            continue
        nodes_result.extend(
            [TextNode(split_nodes[0], TextType.TEXT)]
            + [TextNode(text, text_type) for text in split_nodes[1:-1]]
            + [TextNode(split_nodes[-1], TextType.TEXT)]
        )

    return nodes_result
