import os
import shutil
import sys
from copystatic import copy_static_files_r
from genpage import generate_pages_recursive

if sys.argv:
    basepath = sys.argv[1]
else:
    basepath = "/"

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():

    print("Deleting existing public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files...")
    copy_static_files_r(dir_path_static, dir_path_public)

    generate_pages_recursive(
        dir_path_content, 
        template_path, 
        dir_path_public,
        basepath
    )

main()