from pathlib import Path
import os
import markdown

def generate_page(md_path, template_path, html_path):
    # Ensure parent directories exist
    Path(html_path.parent).mkdir(parents=True, exist_ok=True)

    with open(md_path, "r") as f_md, open(template_path, "r") as f_template, open(html_path, "w") as f_out:
        content_md = f_md.read()
        
        # Extract title (first line starting with # )
        title = "Page"
        for line in content_md.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break

        # Convert markdown to HTML
        content_html = markdown.markdown(content_md)

        # Force <strong>/<em> → <b>/<i> for tests
        content_html = (
            content_html
            .replace("<strong>", "<b>").replace("</strong>", "</b>")
            .replace("<em>", "<i>").replace("</em>", "</i>")
        )

        # Read template and replace placeholders
        template = f_template.read()
        html = template.replace("{{ Title }}", title).replace("{{ Content }}", content_html)

        f_out.write(html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        if os.path.isfile(from_path) and from_path.endswith(".md"):
            # Change .md → .html
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        elif os.path.isdir(from_path):
            # Recurse into subdirectory
            generate_pages_recursive(from_path, template_path, dest_path)