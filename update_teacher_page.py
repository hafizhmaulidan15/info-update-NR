import os
from bs4 import BeautifulSoup

def update_teacher_page():
    file_path = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\teacher.html'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. Update Breadcrumb "Home" -> "Program Kerjasama & Eksisting Mitra"
        # Layout: <div class="it-breadcrumb-list"> <span> <a href="index.html">Home</a> </span> ...
        breadcrumb_list = soup.find('div', class_='it-breadcrumb-list')
        if breadcrumb_list:
            home_link = breadcrumb_list.find('a', href='index.html')
            if home_link and 'Home' in home_link.get_text():
                home_link.string = 'Program Kerjasama & Eksisting Mitra'
                print("Updated Breadcrumb Home link.")
            else:
                print("Breadcrumb Home link not found or text mismatch.")
        else:
            print("Breadcrumb list not found.")
            
        # 2. Update First Card "Millie Patrick"
        # We need to find the card that contains "Millie Patrick".
        # It's an <a> inside <h4> inside <div class="it-team-2-author-info">
        
        # Find all h4 with class 'it-team-2-title'
        titles = soup.find_all('h4', class_='it-team-2-title')
        found = False
        for title in titles:
            link = title.find('a')
            if link and 'Millie Patrick' in link.get_text():
                # Update text
                link.string = 'NANOROBOTIC LEARNING HUB PARTNERS (Kemitraan/Cabang)'
                # Update href
                link['href'] = "https://api.whatsapp.com/send/?phone=6287790005689&text&type=phone_number&app_absent=0"
                found = True
                print("Updated Millie Patrick card.")
                break
        
        if not found:
            print("Millie Patrick card not found (or already updated).")
            
        # 3. Update Second Card "Adelaida Garcia"
        # Find all h4 with class 'it-team-2-title' (re-finding to be safe)
        titles = soup.find_all('h4', class_='it-team-2-title')
        found_adelaida = False
        for title in titles:
            link = title.find('a')
            if link and 'Adelaida Garcia' in link.get_text():
                # Update text
                link.string = 'UPSKILL KNOWLEDGE (Training/Seminar/Workshop)'
                # Update href
                link['href'] = "https://api.whatsapp.com/send/?phone=6287790005689&text&type=phone_number&app_absent=0"
                
                # Remove Social Icons
                # The social div is in the parent's parent usually?
                # Structure:
                # <div class="it-team-2-item">
                #   <div class="it-team-2-thumb-box">
                #     <div class="it-team-2-thumb"> ... <div class="it-team-2-social">...</div> </div>
                #   </div>
                #   <div class="it-team-2-author-info"> <h4>...</h4> </div>
                # </div>
                
                # Go up to it-team-2-item
                author_info = title.find_parent('div', class_='it-team-2-author-info')
                if author_info:
                    item_wrap = author_info.find_parent('div', class_='it-team-2-item')
                    if item_wrap:
                        social_div = item_wrap.find('div', class_='it-team-2-social')
                        if social_div:
                            social_div.decompose()
                            print("Removed social icons for Adelaida Garcia.")
                
                found_adelaida = True
                print("Updated Adelaida Garcia card.")
                break
        
        if not found_adelaida:
            print("Adelaida Garcia card not found (or already updated/renamed).")
            
        # 4. Remove Social Icons from ALL cards
        # User requested: "The icons in the center of the image have been removed. semua di bagian partnernya"
        social_divs = soup.find_all('div', class_='it-team-2-social')
        cnt = 0
        for div in social_divs:
            div.decompose()
            cnt += 1
        print(f"Removed social icons from {cnt} cards (Total cards in file).")
            
        # 5. Update Third Card "David Hernadez"
        titles = soup.find_all('h4', class_='it-team-2-title')
        found_david = False
        for title in titles:
            link = title.find('a')
            if link and 'David Hernadez' in link.get_text():
                # Update text
                link.string = 'UPSKILL COMPETITION (Kompetisi Robotic/Coding/AI)'
                # Update href (redundant if we do all later, but good for specific update)
                link['href'] = "https://api.whatsapp.com/send/?phone=6287790005689&text&type=phone_number&app_absent=0"
                found_david = True
                print("Updated David Hernadez card.")
                break
        
        if not found_david:
            print("David Hernadez card not found (or already updated).")

        # 6. Ensure ALL cards link to WhatsApp
        # User requested: "Diklik, dilink kan dengan WA NanoRobotic itu semua kotak putih di halaman ini ya"
        titles = soup.find_all('h4', class_='it-team-2-title')
        cnt_links = 0
        wa_link = "https://api.whatsapp.com/send/?phone=6287790005689&text&type=phone_number&app_absent=0"
        for title in titles:
            link = title.find('a')
            if link:
                link['href'] = wa_link
                cnt_links += 1
        print(f"Updated links for {cnt_links} cards to WhatsApp.")
    
        # Additional logic: Modify the 3rd card "NANOROBOTIC LEARNING HUB PARTNERS (Kemitraan/Cabang)"
        # Note: Index might be 2 (0-indexed) if it's the 3rd item in the list of found items
        # Let's check based on text content to be sure, or just update index 2 if confident.
        # User request today: "si foto nya ganti... hapus semua tulisan teacher"
        
        target_title_text = "NANOROBOTIC LEARNING HUB PARTNERS (Kemitraan/Cabang)"
        
        # Find all team items to iterate through them
        items = soup.find_all('div', class_='it-team-2-item')

        for item in items:
            title_h4 = item.find('h4', class_='it-team-2-title')
            
            # Remove "Teacher" span from ALL cards
            teacher_span = item.find('span')
            if teacher_span and "Teacher" in teacher_span.get_text():
                teacher_span.decompose()
                print(f"Removed 'Teacher' span from a card.")
                
            # Update Image for specific card: PARTNERS
            if title_h4 and title_h4.find('a') and target_title_text in title_h4.find('a').get_text():
                thumb_div = item.find('div', class_='it-team-2-thumb')
                if thumb_div:
                    img = thumb_div.find('img')
                    if img:
                        img['src'] = 'assets/img/teacher/partner_cabang.png'
                        print("Updated Partner Image for 'NANOROBOTIC LEARNING HUB PARTNERS'.")

            # Update Image for specific card: UPSKILL KNOWLEDGE
            target_upskill_text = "UPSKILL KNOWLEDGE (Training/Seminar/Workshop)"
            if title_h4 and title_h4.find('a') and target_upskill_text in title_h4.find('a').get_text():
                thumb_div = item.find('div', class_='it-team-2-thumb')
                if thumb_div:
                    img = thumb_div.find('img')
                    if img:
                        img['src'] = 'assets/img/teacher/upskill_knowledge.png'
                        print("Updated Image for 'UPSKILL KNOWLEDGE'.")

        # Write back
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(soup.prettify())
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_teacher_page()
