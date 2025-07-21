from copy_dir_contents import clean_directory, copy_files
from generate_html import generate_page


def main():
    clean_directory("public")
    copy_files("static/", "public/")
    generate_page("content/index.md", "template.html", "public/index.html")


if __name__ == "__main__":
    main()
