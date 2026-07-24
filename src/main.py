import os
import shutil
from copystatic import copy_static_files_r
from genpage import generate_page

src_dir = "./static"
dst_public = "./public"
content_src = "./content"
template_src = "./template.html"

def main():

    print("Deleting existing public directory...")
    if os.path.exists(dst_public):
        shutil.rmtree(dst_public)

    print("Copying static files...")
    copy_static_files_r(src_dir, dst_public)

    generate_page(
        os.path.join(content_src, "index.md"), 
        template_src, 
        os.path.join(dst_public, "index.html")
    )

main()