from copy_dir_contents import clean_directory, copy_files
from generate_html import generate_page

from split_nodes import split_nodes_link, split_nodes_image
from textnode import TextNode, TextType


def main():
    clean_directory("public")
    copy_files("static/", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")
    generate_page(
        "content/blog/glorfindel/index.md",
        "template.html",
        "public/blog/glorfindel/index.html",
    )
    generate_page(
        "content/blog/tom/index.md", "template.html", "public/blog/tom/index.html"
    )
    generate_page(
        "content/contact/index.md", "template.html", "public/contact/index.html"
    )
    generate_page(
        "content/blog/majesty/index.md",
        "template.html",
        "public/blog/majesty/index.html",
    )


if __name__ == "__main__":
    main()
