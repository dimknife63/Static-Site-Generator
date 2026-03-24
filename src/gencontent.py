import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f" * {from_path} -> {dest_path}")
    
    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    # Convert Markdown to HTML
    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    # Extract title from Markdown
    title = extract_title(markdown_content)

    # Replace placeholders in template
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    # Replace absolute paths with basepath
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    # Ensure destination directory exists
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    # Write final HTML
    with open(dest_path, "w") as f:
        f.write(template)

def extract_title(md):
    for line in md.split("\n"):
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found in Markdown")