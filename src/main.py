import sys

from copy_dir_contents import clean_directory, copy_files
from generate_html import generate_pages_recursive


def main():
    WEBSITE_DIRECTORY = "docs/"

    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print(basepath)
    clean_directory(WEBSITE_DIRECTORY)
    copy_files("static/", WEBSITE_DIRECTORY)
    generate_pages_recursive("content/", "template.html", WEBSITE_DIRECTORY, basepath)


if __name__ == "__main__":
    main()
