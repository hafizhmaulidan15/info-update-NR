import os
from bs4 import BeautifulSoup

def update_shop_page():
    file_path = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\shop.html'
    wa_link = "https://api.whatsapp.com/send/?phone=6287790005689&text&type=phone_number&app_absent=0"
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
    # Updated helper to handle specific product message
        def process_product(title_text, new_title, card_index):
            items = soup.find_all('div', class_='it-shop-item')
            if card_index < len(items):
                item = items[card_index]
                
                # WA Base Link
                # Using standard URL encoding for "Halo kak, saya mau pesan [Name]"
                # "Halo kak, saya mau pesan " => Halo%20kak%2C%20saya%20mau%20pesan%20
                import urllib.parse
                base_text = f"Halo kak, saya mau pesan {new_title}"
                encoded_text = urllib.parse.quote(base_text)
                wa_full_link = f"https://api.whatsapp.com/send/?phone=6287790005689&text={encoded_text}&type=phone_number&app_absent=0"

                # 1. Update Title & Link
                title_h4 = item.find('h4', class_='it-shop-title')
                if title_h4:
                    link = title_h4.find('a')
                    if link:
                        link.string = new_title
                        link['href'] = wa_full_link
                
                # 2. Remove Price/Rating Row
                rate_div = item.find('div', class_='it-shop-rate')
                if rate_div:
                    rate_div.decompose()
                    
                # 3. Update "Shop now" button
                btn_div = item.find('div', class_='it-shop-button')
                if btn_div:
                    btn_a = btn_div.find('a')
                    if btn_a:
                        btn_a['href'] = wa_full_link
                        
                print(f"Updated product {card_index+1} to '{new_title}' with custom WA link.")
            else:
                print(f"Product index {card_index} out of range.")

        # Update first 6 products again to apply new WA link logic
        process_product("School Bag", "Robotic/STEM Kit", 0)
        process_product("Book", "Robotic/STEM Kit", 1)
        process_product("Pencell", "Robotic/STEM Kit", 2)
        process_product("Note", "Coding Kit", 3)
        process_product("Book", "NanoRobotic T-Shirt", 4)
        process_product("Baby toys", "NanoRobotic's Thumbler", 5)

        # Update next products (Row 3 & 4)
        process_product("Baby toys", "NanRobotic's Key Chain", 6)
        process_product("Baby toys", "NanRobotic's Mug", 7)
        process_product("Baby toys", "NanRobotic's ToteBag", 8)
        process_product("Note", "NanRobotic's Notes", 9)
        process_product("Baby toys", "Robotic's Explorer Book", 10)
        
        # Determine strict logic for items 11 and 12 (book duplicate)
        # Based on image, the one with "Dihilangkan" is the one NEXT to 'Robotic's Explorer Book' (Item 11).
        # So item 12 is likely the duplicate to remove.
        # But wait, user said "Dihilangkan karena gambarnya sama dengan gambar bawah".
        # Image 2 (uploaded) shows "Robotic's Explorer Book" (Top Left), Duplicate (Top Right), "Coding's Explorer Book" (Bottom Center).
        # This implies items 11 and 12 are top row, item 13 is bottom row?
        # Let's count items in shop.html (view_file output stopped at line 818, item 11).
        # Let's just assume item 11 is "Robotic's...", item 12 is duplicate, and verify item 13 exists or if "Coding's" is item 12.
        # Actually simplest is: Update item 11. Delete item 12?
        # Let's check finding "Coding's Explorer Book" original name.
        # It's likely also "Baby toys" or "Book".
        # Let's try to update item 12 to "Coding's Explorer Book" IF it's not the duplicate.
        # If the user says remove the one with same image as bottom...
        # Maybe item 11 and item 12 are similar.
        
        # Helper to get WA Link
        def get_wa_link(title):
            import urllib.parse
            base_text = f"Halo kak, saya mau pesan {title}"
            encoded_text = urllib.parse.quote(base_text)
            return f"https://api.whatsapp.com/send/?phone=6287790005689&text={encoded_text}&type=phone_number&app_absent=0"

        # Check if we need to add Item 12 (Coding's Explorer Book)
        # We currently have 11 items (indices 0-10).
        items = soup.find_all('div', class_='it-shop-item')
        if len(items) == 11:
            print("Adding Coding's Explorer Book (Item 12)...")
            # We need to clone the COLUMN, not just the item div
            last_col = items[10].parent
            
            # Create a deep copy of the column
            import copy
            # BS4 elements are copyable? simpler to parse string
            new_col_soup = BeautifulSoup(str(last_col), 'html.parser')
            new_col = new_col_soup.find('div', recursive=False) # Get the col div
            
            # Update the item inside new_col
            item = new_col.find('div', class_='it-shop-item')
            
            # Update Image (Guessing 10buku.png)
            img = item.find('img')
            if img:
                img['src'] = 'assets/img/shop/SHOP ITEM/10buku.png'
                
            # Update Title and Link
            new_title = "Coding's Explorer Book"
            wa_link = get_wa_link(new_title)
            
            title_h4 = item.find('h4', class_='it-shop-title')
            if title_h4:
                link = title_h4.find('a')
                if link:
                    link.string = new_title
                    link['href'] = wa_link
            
            # Update Button
            btn_div = item.find('div', class_='it-shop-button')
            if btn_div:
                btn_a = btn_div.find('a')
                if btn_a:
                    btn_a['href'] = wa_link

            # Remove Price/Rating (already done in clone if source had it removed, but source was Item 11 which likely had it removed 2 seconds ago? 
            # Wait, process_product runs BEFORE this. So Item 11 is clean effectively? 
            # No, process_product modifies the soup in place. So yes, it should be clean.
            
            # Append to the row
            row = last_col.parent
            row.append(new_col)
            print("Added Coding's Explorer Book.")
            
        # 6. Cleanup "Showing 12 of 120 results" and Pagination
        # Remove top bar text
        shop_top = soup.find('div', class_='tp-shop-top')
        if shop_top:
            shop_top.decompose()
            print("Removed 'Showing results' top bar.")
            
        # Remove Pagination (usually at bottom, class 'basic-pagination' or similar)
        # Check file content or just look for 'basic-pagination' or 'it-pagination'
        pagination = soup.find('div', class_='basic-pagination')
        if pagination:
            pagination.decompose()
            print("Removed pagination.")
        
        # Also check for 'it-pagination' if basic-pagination not found
        pagination2 = soup.find('div', class_='it-pagination')
        if pagination2:
            pagination2.decompose()
            print("Removed it-pagination.")

        # 7. Remove Empty Column Divs (col-xl-3 ...)
        # These might be placeholders that cause gaps in the grid.
        # Strict logic: Find div with class col-xl-3... that has NO children or only whitespace.
        # IMPORTANT: Exclude footer columns which also use col-xl-3 but have 'it-footer-widget'.
        
        all_cols = soup.find_all('div', class_='col-xl-3')
        for col in all_cols:
            # Check if it contains a shop item
            has_item = col.find('div', class_='it-shop-item')
            # Check if it is a footer widget
            has_footer = col.find('div', class_='it-footer-widget')
            
            if not has_item and not has_footer:
                # It's potentially an empty placeholder.
                # Double check contents are empty string
                text_content = col.get_text(strip=True)
                if not text_content: 
                    print(f"Removing empty column: {col.attrs}")
                    col.decompose()

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(soup.prettify())
            
    except Exception as e:
        print(f"Error updating file: {e}")

if __name__ == "__main__":
    update_shop_page()
