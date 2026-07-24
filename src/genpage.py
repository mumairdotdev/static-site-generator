import os
from blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if "# " in line:
            return line[2:].strip()
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path, basepath):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        md = f.read()
    with open(template_path, "r") as f:
        template = f.read()

    content = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    template = template.replace("href=/", f"href={basepath}").replace("src=/", f"src={basepath}")
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, filename)
        dst_path = os.path.join(dest_dir_path, filename)
        print(f"Converting {src_path} to {dst_path}")
        if os.path.isfile(src_path):
            dst_path = dst_path.replace(".md", ".html")
            generate_page(src_path, template_path, dst_path, basepath)
        else:
            generate_pages_recursive(src_path, template_path, dst_path, basepath)