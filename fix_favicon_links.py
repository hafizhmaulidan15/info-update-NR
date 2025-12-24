import os
from bs4 import BeautifulSoup

def fix_favicon_links():
    directory = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden'
    
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                try:
                    content = f.read()
                except UnicodeDecodeError:
                    print(f"Skipping {filename} due to encoding error")
                    continue
            
            soup = BeautifulSoup(content, 'html.parser')
            modified = False
            
            # Find favicon link
            # <link href="assets/img/logo/favicon.png" rel="shortcut icon" type="image/x-icon"/>
            
            links = soup.find_all('link', rel='shortcut icon')
            for link in links:
                href = link.get('href', '')
                if 'favicon.png' in href:
                    current_type = link.get('type')
                    if current_type != 'image/png':
                        link['type'] = 'image/png'
                        modified = True
                        print(f"Updated favicon type in {filename}")
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f_out:
                    f_out.write(soup.prettify())

if __name__ == "__main__":
    fix_favicon_links()
