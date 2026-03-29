import os

def generate_pages_recursive(content_dir, template_path, output_dir, basepath="/"):
    """
    Recursively generate HTML pages from markdown content.
    """
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                rel_path = os.path.relpath(md_path, content_dir)
                html_rel_path = rel_path.replace(".md", ".html")
                output_path = os.path.join(output_dir, html_rel_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                generate_page(md_path, template_path, output_path, basepath)

def generate_page(md_path, template_path, output_path, basepath="/"):
    """
    Generate a single HTML page from a markdown file.
    """
    # Read markdown
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    title = lines[0].strip("# \n")
    content = "".join(lines[1:])

    # Read template
    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace placeholders
    html = html.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content)

    # Ensure basepath has exactly one slash at start, none at end
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    if not basepath.endswith("/"):
        basepath += "/"

    # Replace href/src paths
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')

    # Write HTML
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)