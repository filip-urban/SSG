from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextType, TextNode


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        for image in images:
            delimiter = f"![{image[0]}]({image[1]})"
            split_text, node.text = node.text.split(delimiter, maxsplit=1)
            if split_text:
                new_nodes.append(TextNode(split_text, TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, url=image[1]))
        if node.text:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text_type == TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        for link in links:
            delimiter = f"[{link[0]}]({link[1]})"
            split_text, node.text = node.text.split(delimiter, maxsplit=1)
            if split_text:
                new_nodes.append(TextNode(split_text, TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, url=link[1]))
        if node.text:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
    return new_nodes


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
