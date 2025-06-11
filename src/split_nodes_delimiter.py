from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes_result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes_result.extend([node])
            continue
        text = node.text
        while text:
            if text[: len(delimiter)] == delimiter:
                split_result = text[len(delimiter) :].split(delimiter, maxsplit=1)
                if len(split_result) < 2:
                    nodes_result.extend([TextNode(text, TextType.TEXT)])
                    break
                split_text, text = split_result[0], split_result[1]
                nodes_result.extend([TextNode(split_text, text_type)])
            else:
                split_result = text.split(delimiter, maxsplit=1)
                if len(split_result) < 2:
                    nodes_result.extend([TextNode(text, TextType.TEXT)])
                    break
                split_text, text = split_result[0], split_result[1]
                if split_result[1]:
                    text = delimiter + text
                nodes_result.extend([TextNode(split_text, TextType.TEXT)])
    return nodes_result
