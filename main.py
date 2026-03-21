import os
import sys
import pathlib
import markdown
import re

def generate_page(content_path, template_path, dest_path, basepath):
    # 1. Read Markdown content
    with open(content_path, "r", encoding="utf-8") as f:
        content_md = f.read()

    # 2. Convert Markdown to HTML
    content_html = markdown.markdown(content_md)

    # 3. Fix blockquotes: remove extra <p> inside <blockquote>
    content_html = re.sub(
        r"<blockquote>\s*<p>(.*?)</p>\s*</blockquote>",
        r"<blockquote>\1</blockquote>",
        content_html,
        flags=re.DOTALL
    )

    # 4. Convert <strong>/<em> to <b>/<i>
    content_html = (
        content_html
        .replace("<strong>", "<b>").replace("</strong>", "</b>")
        .replace("<em>", "<i>").replace("</em>", "</i>")
    )

    # 5. Read template
    with open(template_path, "r", encoding="utf-8") as f:
        template_html = f.read()

    # 6. Inject content and adjust basepath
    final_html = template_html.replace("{{ Content }}", content_html)
    final_html = final_html.replace('href="/', f'href="{basepath}')
    final_html = final_html.replace('src="/', f'src="{basepath}')

    # 7. Ensure destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # 8. Write final HTML
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # Walk through every file in content directory
    for entry in os.listdir(dir_path_content):
        full_entry_path = os.path.join(dir_path_content, entry)
        if os.path.isfile(full_entry_path) and entry.endswith(".md"):
            rel_path = os.path.relpath(full_entry_path, dir_path_content)
            dest_path = os.path.join(dest_dir_path, rel_path)
            dest_path = os.path.splitext(dest_path)[0] + ".html"
            generate_page(full_entry_path, template_path, dest_path, basepath)
        elif os.path.isdir(full_entry_path):
            generate_pages_recursive(full_entry_path, template_path, dest_dir_path, basepath)

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    content_dir = "content"
    template_path = "template.html"
    dest_dir = "docs"  # GitHub Pages uses docs/

    generate_pages_recursive(content_dir, template_path, dest_dir, basepath)
    print("Site generated successfully!")

# Correct placement — this must be outside the main() function
if __name__ == "__main__":
    main()