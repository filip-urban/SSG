from copy_dir_contents import clean_directory, copy_files
from generate_html import generate_pages_recursive


def main():
    clean_directory("public")
    copy_files("static/", "public/")
    generate_pages_recursive("content", "template.html", "public")


if __name__ == "__main__":
    main()
