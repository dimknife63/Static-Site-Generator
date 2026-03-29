import os
import shutil
import sys

from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

# Paths
dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

# Default basepath for local testing
default_basepath = "/"

def main():
    # Get basepath from CLI argument or default
    basepath = sys.argv[1] if len(sys.argv) > 1 else default_basepath

    print("Deleting docs directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_docs)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_docs, basepath)

if __name__ == "__main__":
    main()