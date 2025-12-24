import os
from bs4 import BeautifulSoup

def fix_retail_dropdown():
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
            
            # Find the Retail menu item
            # Look for <a> with text "Retail" (usually with an icon inside)
            # OR look for <li> with Retail text.
            
            # Strategy: Find all <li> with class 'has-dropdown'
            # Check if it contains "Retail" text directly or inside <a>
            
            lis = soup.find_all('li', class_='has-dropdown')
            for li in lis:
                a_tag = li.find('a')
                if a_tag and "Retail" in a_tag.get_text(strip=True):
                    # Found the Retail dropdown!
                    
                    # 1. Remove 'has-dropdown' class
                    if 'has-dropdown' in li['class']:
                        li['class'].remove('has-dropdown')
                    
                    # 2. Remove the submenu <ul>
                    submenu = li.find('ul', class_='submenu')
                    if submenu:
                        submenu.decompose()
                    
                    # 3. Update the <a> href to 'shop.html' (if it was '#')
                    # User didn't explicitly say "link to shop.html", but implicit "Retail" usually means Shop.
                    # And previously "Shop" was a submenu item linking to shop.html.
                    if a_tag['href'] == '#' or a_tag['href'] == '':
                        a_tag['href'] = 'shop.html'
                    
                    modified = True
                    print(f"Fixed Retail dropdown in {filename}")
            
            if modified:
                with open(filepath, 'w', encoding='utf-8') as f_out:
                    f_out.write(soup.prettify())

if __name__ == "__main__":
    fix_retail_dropdown()
