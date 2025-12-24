from bs4 import BeautifulSoup
import os

def populate_brand_images():
    file_path = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\teacher.html'
    
    # List of actual images from the directory listing
    brand_images = [
        "Botani Square.png",
        "Farmers Market.png",
        "Ibnu Hajar.png",
        "Kesatuan.png",
        "Lazu.png",
        "Mangga Dual Mall.png",
        "Mizan.png",
        "SA Al Giva.png",
        "SDIT Al Ikhlas.png",
        "SDIT Al Munawar.png",
        "SDIT Kemuning.png",
        "SMP Lazuardi.png",
        "TSM Mall Cibubur.png",
        "Bina Bangsa.png"
    ]
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find the brand slider wrapper
    brand_active = soup.find('div', class_='it-brand-active')
    if not brand_active:
        print("it-brand-active container not found")
        return

    swiper_wrapper = brand_active.find('div', class_='swiper-wrapper')
    if not swiper_wrapper:
        print("swiper-wrapper not found")
        return
        
    # Clear existing placeholder slides
    swiper_wrapper.clear()
    
    # Add new slides for each image
    for img_name in brand_images:
        # Create slide structure
        # <div class="swiper-slide">
        #   <div class="it-brand-item text-center">
        #     <img src="..." alt="" loading="lazy">
        #   </div>
        # </div>
        
        slide = soup.new_tag('div', attrs={'class': 'swiper-slide'})
        item_div = soup.new_tag('div', attrs={'class': 'it-brand-item text-center'})
        
        # URL encode filename just in case of spaces (though newer browsers handle it, better safe)
        # Actually simple string is usually fine in src for local files if handled by browser, 
        # but pure spaces might be an issue. Let's just use the name as is first.
        # Be careful with "Mangga DualÂ Mall.png" - the list_dir output had a weird char? 
        # "Mangga Dual\u00a0Mall.png" (NBSP). Let's be careful.
        # I'll stick to simple replacing spaces with %20 if needed, or just trusting the browser.
        
        src_path = f"assets/img/brand/{img_name}"
        img = soup.new_tag('img', attrs={'src': src_path, 'alt': img_name.split('.')[0], 'loading': 'lazy'})
        
        # Optional: Force a max height for logos so they align well? 
        # The CSS for .it-brand-item img might handle it. 
        # Let's add a style to be safe or rely on main.css.
        # main.css usually handles it.
        
        item_div.append(img)
        slide.append(item_div)
        swiper_wrapper.append(slide)
        
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())
        print(f"Populated {len(brand_images)} brand images into slider.")

if __name__ == "__main__":
    populate_brand_images()
