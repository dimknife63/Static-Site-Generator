import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    """Recursively generate pages from content/ to docs/"""
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    """Generate a single HTML page from markdown"""
    print(f" * {from_path} {template_path} -> {dest_path}")

    # Read markdown content
    with open(from_path, "r") as f:
        markdown_content = f.read()

    # Read HTML template
    with open(template_path, "r") as f:
        template = f.read()

    # Convert markdown to HTML
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Extract title from first line starting with "# "
    title = extract_title(markdown_content)

    # Replace placeholders in template
    page = template.replace("{{ Title }}", title)
    page = page.replace("{{ Content }}", html)
    page = page.replace('href="/', f'href="{basepath}')
    page = page.replace('src="/', f'src="{basepath}')

    # Ensure destination directory exists
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    # Write final HTML to file
    with open(dest_path, "w") as f:
        f.write(page)


def extract_title(md):
    """Return the first line starting with # as the title"""
    for line in md.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found in markdown")