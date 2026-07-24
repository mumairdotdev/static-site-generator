import os
import shutil
from copystatic import copy_static_files_r

src_dir = "./static"
dst_public = "./public"

def main():

    print("Deleting existing public directory...")
    if os.path.exists(dst_public):
        shutil.rmtree(dst_public)

    print("Copying static files...")
    copy_static_files_r(src_dir, dst_public)

main()