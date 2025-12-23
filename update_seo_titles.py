import os
import re

# Define the directory to search (current directory)
search_dir = r"d:\Hafizh\Matra\Web Nanorobotic\Template cobaan\kiden"

# The old title regex (to catch slight variations if any, or just fixed string)
# The user specified: <title>Kiden - Kids, Children, School & Kindergarten HTML Template</title>
# But let's be safe and match the tag content.
old_title_pattern = re.compile(r"<title>.*Kiden.*</title>", re.IGNORECASE)
new_title = "<title>NANOROBOTIC - Robotic, Coding, AI</title>"

count = 0

print(f"Scanning directory: {search_dir}")

for root, dirs, files in os.walk(search_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                if old_title_pattern.search(content):
                    new_content = old_title_pattern.sub(new_title, content)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")
                    count += 1
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print(f"Total files updated: {count}")
