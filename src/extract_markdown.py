import re
import sys


def extract_markdown_images(text):
    regex = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(regex, text)


def extract_markdown_links(text):
    regex = r"[^!]\[(.*?)\]\((.*?)\)"
    return re.findall(regex, text)


def extract_title(markdown):
    try:
        with open(markdown) as md:
            for line in md:
                if line.startswith("# "):
                    return line[2:].strip()
            raise Exception("Invalid markdown: no h1 header present in the markdown.")
    except OSError as err:
        print(err)
        sys.exit(1)
