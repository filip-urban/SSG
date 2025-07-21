import sys
import os
import pathlib

from block_to_html import markdown_to_html_node
from extract_markdown import extract_title


def read_file(filename):
    try:
        with open(filename, "r") as file_h:
            return file_h.read()
    except OSError as err:
        print(err)
        sys.exit(1)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = read_file(from_path)
    template = read_file(template_path)
    html = markdown_to_html_node(md_file).to_html()
    title = extract_title(from_path)
    html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    pathlib.Path(os.path.dirname(dest_path)).mkdir(parents=True, exist_ok=True)
    try:
        with open(dest_path, "w+") as dest_file_h:
            dest_file_h.write(html_page)
    except OSError as err:
        print(err)
        sys.exit(1)
