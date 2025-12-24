import os
import sys
from bs4 import BeautifulSoup, Tag

def fix_menu(filepath):
    print(f"Processing {filepath}...")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        modified = False
        
        # Target the specific container: .it-header-menu
        nav_container = soup.find('div', class_='it-header-menu')
        
        if nav_container:
            # 1. Check for existing "Artikel" menu INSIDE the header
            artikel_link = None
            for a in nav_container.find_all('a'):
                if a.get('href') and ('blog.html' in a.get('href')):
                    # Check text loosely to match "Artikel"
                    if "Artikel" in a.get_text():
                        artikel_link = a
                        break
            
            if artikel_link:
                # Case 1: Exists in header. Fix it.
                parent_li = artikel_link.find_parent('li')
                if parent_li:
                    # Remove has-dropdown class
                    if parent_li.get('class') and 'has-dropdown' in parent_li.get('class'):
                        parent_li['class'] = [c for c in parent_li['class'] if c != 'has-dropdown']
                        modified = True
                        print("  Fixed: removed has-dropdown.")
                    
                    # Remove submenu
                    submenu = parent_li.find('ul', class_='submenu')
                    if submenu:
                        submenu.decompose()
                        modified = True
                        print("  Fixed: removed submenu.")
                    else:
                        print("  Checked: no submenu found.")
            else:
                # Case 2: Missing in header. Restore it.
                print("  Missing in header. Restoring...")
                
                # Find "Contact" or "Retail" reference in header
                contact_link = None
                for a in nav_container.find_all('a'):
                    if a.get('href') and ('contact.html' in a.get('href')):
                         contact_link = a
                         break
                
                if contact_link:
                    contact_li = contact_link.find_parent('li')
                    if contact_li:
                        # Create new li
                        new_Li = soup.new_tag("li")
                        # Emulate the structure
                        # <li><a href="blog.html"><span><img ...></span>Artikel</a></li>
                        
                        new_a = soup.new_tag("a", href="blog.html")
                        
                        new_span = soup.new_tag("span")
                        new_img = soup.new_tag("img", src="ICON/ICON/6artikel.svg", alt="Ikon Beranda", width="16", height="16", loading="lazy")
                        new_span.append(new_img)
                        
                        new_a.append(new_span)
                        new_a.append(" Artikel")
                        
                        new_Li.append(new_a)
                        
                        # Insert before contact_li
                        contact_li.insert_before(new_Li)
                        modified = True
                        print("  Restored 'Artikel' menu in header.")
                else:
                    print("  Could not find 'Contact' menu to insert before.")
        else:
            print("  No .it-header-menu found. Skipping header logic.")

        # ALWAYS save to apply prettify formatting as requested ("rapihin kodenya")
        # unless it's a file we shouldn't touch? No, user said "semua halaman".
        # But only if it's an HTML file that looks like a page.
        
        html_out = soup.prettify()
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_out)
        print(f"Successfully processed and formatted {filepath}")

            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    
    if os.path.isfile(target):
        fix_menu(target)
    elif os.path.isdir(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                if file.endswith(".html"):
                    fix_menu(os.path.join(root, file))
