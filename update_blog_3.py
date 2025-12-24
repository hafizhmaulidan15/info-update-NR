from bs4 import BeautifulSoup

def update_blog_item():
    file_path = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\blog.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find all blog items
    blog_items = soup.find_all('div', class_='it-blog-item')
    
    if len(blog_items) >= 3:
        item = blog_items[2] # Index 2 is the 3rd item
        
        # Update Date
        date_span = item.find('span') 
        # Usually date is in <div class="it-blog-date"><span>...</span></div>
        # Let's inspect structure more carefully if needed, but usually span inside date div
        date_div = item.find('div', class_='it-blog-date')
        if date_div:
            span = date_div.find('span')
            if span:
                span.string = "24 Desember 2025"
                print("Updated Date.")
                
        # Update Title
        title_h4 = item.find('h4', class_='it-blog-title')
        if title_h4:
            link = title_h4.find('a')
            if link:
                link.string = "MEMPERSIAPKAN GENERASI FUTURE-READY: PERAN PENDIDIKAN TEKNOLOGI SEJAK DINI"
                print("Updated Title.")
                
        # Update Image?
        # User image shows placeholder "340 X 234" in gray box.
        # If the user provided a title, maybe they want the image to match? 
        # But they didn't provide an image file, only screenshot.
        # So we leave the image as is (placeholder) or check if we have one.
        # The user request only mentioned "perbaiki tanggal waktu dan judulnya".
        
    else:
        print("Less than 3 blog items found.")

    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())

if __name__ == "__main__":
    update_blog_item()
