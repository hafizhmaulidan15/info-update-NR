import os
from bs4 import BeautifulSoup

def fix_partner_menu():
    # Get current directory
    current_dir = os.getcwd()
    
    # List all HTML files
    html_files = [f for f in os.listdir(current_dir) if f.endswith('.html')]
    
    print(f"Found {len(html_files)} HTML files to process.")
    
    for filename in html_files:
        file_path = os.path.join(current_dir, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            soup = BeautifulSoup(content, 'html.parser')
            
            # Find the Partner menu item
            # It's an li with text "Partner", usually containing an img and text inside 'a' inside 'li'
            
            # Strategy: Find the <a> tag with href="teacher.html" and text "Partner"
            # Or find <span>Partner</span> inside <a>
            # But "Partner" text might be inside the <a> but after <span>
            
            # Let's search for <a> tags where text contains "Partner" or href="teacher.html"
            # Based on view_file:
            # <li class="has-dropdown">
            #  <a href="teacher.html">... Partner</a>
            
            partner_link = None
            for a in soup.find_all('a'):
                if a.get('href') == 'teacher.html' and 'Partner' in a.get_text():
                    partner_link = a
                    break
            
            if partner_link:
                # Get the parent <li>
                li_tag = partner_link.parent
                if li_tag.name == 'li':
                    # Remove 'has-dropdown' class
                    if 'has-dropdown' in li_tag.get('class', []):
                        li_tag['class'] = [c for c in li_tag['class'] if c != 'has-dropdown']
                        print(f"  Removed 'has-dropdown' from {filename}")
                    
                    # Remove submenu <ul>
                    submenu = li_tag.find('ul', class_='submenu')
                    if submenu:
                        submenu.decompose()
                        print(f"  Removed submenu from {filename}")
                    
                    # Save changes
                    with open(file_path, 'w', encoding='utf-8') as f_out:
                        f_out.write(soup.prettify())
                else:
                    print(f"  Partner link parent is not LI in {filename}??")
            else:
                print(f"  Partner menu item not found in {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    fix_partner_menu()
