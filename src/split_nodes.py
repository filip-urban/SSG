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
