from gencontent import generate_pages_recursive

def main():
    dir_path_content = "content"
    template_path = "template.html"
    dir_path_public = "public"

    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

if __name__ == "__main__":
    main()
