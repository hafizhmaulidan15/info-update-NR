from bs4 import BeautifulSoup

def update_slider_to_brand():
    file_path = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\teacher.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # 1. Find the bottom slider we just made. It was in a 'row mt-60' inside 'container' inside 'it-team-2-area'.
    team_area = soup.find('div', class_='it-team-2-area')
    if not team_area:
        print("it-team-2-area not found")
        return

    container = team_area.find('div', class_='container')
    rows = container.find_all('div', class_='row')
    
    # The last row should be the slider row we added
    if len(rows) < 2:
        print("Not enough rows found. Required separate static and slider rows.")
        return
        
    slider_row = rows[-1] 
    
    # Verify it has swiper container just to be safe
    if not slider_row.find('div', class_='swiper-container'):
        print("Last row doesn't look like the slider row. Aborting.")
        # return # actually, let's proceed with caution or just replacing the last row if possible.
        
    # 2. Create the New Brand Slider Structure
    # Based on index.html:
    # <div class="it-brand-area pt-120 pb-120 theme-bg"> (Maybe remove theme-bg or keep purple per image?)
    # user image background is light purple. index.html brand area might be just white or theme-bg.
    # Let's inspect the user image again... It has a title "Telah Dipercaya Oleh Mitra Kami"
    
    # We will replace the entire "Slider Row" with a new "Brand Section Div" OR just put the brand HTML inside the row.
    # The Brand structure in index.html is:
    # <div class="it-brand-area pt-120 pb-120 theme-bg"> ... container ... swiper ... </div>
    
    # Since we are inside 'it-team-2-area' which has its own padding/bg, maybe we should close that div and append a new brand div?
    # Or just insert the brand slider content here.
    
    # Let's use clean HTML replacement for that row.
    
    new_html = """
    <div class="row mt-60 align-items-center justify-content-center">
        <div class="col-xl-12">
            <div class="it-section-title-box text-center mb-50">
                <span class="it-section-subtitle">Telah Dipercaya Oleh</span>
                <h4 class="it-section-title">Mitra Kami</h4>
            </div>
        </div>
        <div class="col-xl-12">
            <div class="it-brand-active swiper-container">
                <div class="swiper-wrapper">
                    <div class="swiper-slide">
                        <div class="it-brand-item text-center">
                            <img src="assets/img/brand/brand-1-1.png" alt="" loading="lazy">
                        </div>
                    </div>
                    <div class="swiper-slide">
                        <div class="it-brand-item text-center">
                            <img src="assets/img/brand/brand-1-2.png" alt="" loading="lazy">
                        </div>
                    </div>
                    <div class="swiper-slide">
                        <div class="it-brand-item text-center">
                            <img src="assets/img/brand/brand-1-3.png" alt="" loading="lazy">
                        </div>
                    </div>
                    <div class="swiper-slide">
                        <div class="it-brand-item text-center">
                            <img src="assets/img/brand/brand-1-4.png" alt="" loading="lazy">
                        </div>
                    </div>
                     <div class="swiper-slide">
                        <div class="it-brand-item text-center">
                            <img src="assets/img/brand/brand-1-5.png" alt="" loading="lazy">
                        </div>
                    </div>
                     <div class="swiper-slide">
                        <div class="it-brand-item text-center">
                            <img src="assets/img/brand/brand-1-1.png" alt="" loading="lazy">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    
    # Parse the new HTML
    new_soup = BeautifulSoup(new_html, 'html.parser')
    
    # Replace the old slider row with new brand row
    slider_row.replace_with(new_soup)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())
        print("Updated bottom slider to Brand/Mitra slider.")

if __name__ == "__main__":
    update_slider_to_brand()
