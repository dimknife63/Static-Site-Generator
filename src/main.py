import os
import sys

# Base path for GitHub Pages
basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

# Sample posts structure
posts = [
    {"title": "Majesty", "slug": "majesty", "content": "<p>This is Majesty post.</p>"},
    {"title": "Tom", "slug": "tom", "content": "<p>This is Tom post.</p>"},
]

TEMPLATE_FILE = "template.html"
OUTPUT_DIR = "docs"

# Load template
with open(TEMPLATE_FILE, "r") as f:
    template = f.read()

def generate_page(title, content, output_path, basepath="/"):
    html = template.replace("{{ Title }}", title).replace("{{content}}", content)
    html = html.replace('href="/', f'href="{basepath}')
    html = html.replace('src="/', f'src="{basepath}')
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(html)

def generate_pages_recursive(posts, output_dir="docs", basepath="/"):
    # Generate homepage
    generate_page("Home", "<h1>Welcome to my site</h1>", os.path.join(output_dir, "index.html"), basepath)
    
    # Generate blog posts
    for post in posts:
        post_dir = os.path.join(output_dir, "blog", post["slug"])
        output_path = os.path.join(post_dir, "index.html")
        generate_page(post["title"], post["content"], output_path, basepath)

# Run generator
generate_pages_recursive(posts, OUTPUT_DIR, basepath)
print(f"Site generated successfully in {OUTPUT_DIR}/")