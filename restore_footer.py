from bs4 import BeautifulSoup

def restore_footer():
    target_file = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\shop.html'
    source_file = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\about-us.html'
    
    try:
        # Read Source
        with open(source_file, 'r', encoding='utf-8') as f:
            source_content = f.read()
        source_soup = BeautifulSoup(source_content, 'html.parser')
        footer = source_soup.find('footer')
        
        # Read Target
        with open(target_file, 'r', encoding='utf-8') as f:
            target_content = f.read()
        target_soup = BeautifulSoup(target_content, 'html.parser')
        
        # Check if footer exists
        if target_soup.find('footer'):
            print("Footer already exists in target.")
            # Optional: replace if broken? But let's assume if it exists, it's fine or we manually check.
            # But earlier check showed it missing.
            # If it exists but is partial, decompose it first.
            target_soup.find('footer').decompose()
        
        # Insert Footer
        # Footer usually comes after main
        main = target_soup.find('main')
        if main:
            main.insert_after(footer)
            print("Footer restored.")
        else:
            print("Could not find main tag to insert footer after.")
            
        with open(target_file, 'w', encoding='utf-8') as f_out:
            f_out.write(target_soup.prettify())
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    restore_footer()
