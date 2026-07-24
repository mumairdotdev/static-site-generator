import os
import shutil

def copy_static_files_r(src_dir, dst_public):
    if not os.path.exists(dst_public):
        os.mkdir(dst_public)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_public, item)
        print(f"Copying {src_path} to {dst_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_static_files_r(src_path, dst_path)
