import sys
import os
import pathlib

from block_to_html import markdown_to_html_node
from extract_markdown import extract_title
from copy_dir_contents import get_list_of_source_paths


def read_file(filename):
    try:
        with open(filename, "r") as file_h:
            return file_h.read()
    except OSError as err:
        print(err)
        sys.exit(1)


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    md_file = read_file(from_path)
    template = read_file(template_path)
    html = markdown_to_html_node(md_file).to_html()
    title = extract_title(from_path)
    html_page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
    html_page = html_page.replace('href="/', f'href="{basepath}')
    html_page = html_page.replace('src="/', f'src="{basepath}')
    pathlib.Path(os.path.dirname(dest_path)).mkdir(parents=True, exist_ok=True)
    try:
        with open(dest_path, "w+") as dest_file_h:
            dest_file_h.write(html_page)
    except OSError as err:
        print(err)
        sys.exit(1)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_paths = get_list_of_source_paths(dir_path_content)
    for path in content_paths:
        dest_path = path.replace(dir_path_content, dest_dir_path, 1)
        if path[-1] == "/":
            os.mkdir(dest_path)
        else:
            if dest_path[-3:] == ".md":
                dest_path = dest_path[:-3] + ".html"
            else:
                dest_path = dest_path + ".html"
            generate_page(path, template_path, dest_path, basepath)
