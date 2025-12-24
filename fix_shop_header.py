from bs4 import BeautifulSoup

def fix_shop_header():
    file_path = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\shop.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # helper to find the header row
    header_area = soup.find('div', class_='it-header-area')
    if not header_area: 
        print("Header area not found")
        return

    container = header_area.find('div', class_='container')
    header_wrap = container.find('div', class_='it-header-wrap')
    row = header_wrap.find('div', class_='row')
    
    # Check if col-xl-3 already exists
    col_right = row.find('div', class_='col-xl-3')
    if col_right:
        print("col-xl-3 already exists. Checking content...")
        # Maybe it exists but is empty?
        if not col_right.find('div', class_='it-header-right'):
             print("col-xl-3 is missing content. Fixing...")
             col_right.decompose() # Remove and recreate
        else:
             print("Button seems to confirm exist. Skipping.")
             return

    # Create the missing column
    new_col = soup.new_tag('div', attrs={'class': 'col-xl-3 col-6'})
    
    # Content for the new column
    # <div class="it-header-right d-none d-xl-flex align-items-center justify-content-end">
    #  <div class="it-header-button">
    #   <a class="it-btn theme-2-bg circle-effect" href="https://api.whatsapp.com/send/?phone=6287790005689&amp;text&amp;type=phone_number&amp;app_absent=0">
    #    <span>BOOK FREE TRIAL...</span>
    #   </a>
    #  </div>
    # </div>
    # <div class="it-header-bar d-xl-none text-end">...</div>

    # 1. Header Right
    header_right = soup.new_tag('div', attrs={'class': 'it-header-right d-none d-xl-flex align-items-center justify-content-end'})
    header_btn_div = soup.new_tag('div', attrs={'class': 'it-header-button'})
    
    btn_link = soup.new_tag('a', attrs={
        'class': 'it-btn theme-2-bg circle-effect',
        'href': 'https://api.whatsapp.com/send/?phone=6287790005689&text&type=phone_number&app_absent=0'
    })
    
    btn_span = soup.new_tag('span')
    btn_span.string = "BOOK FREE TRIAL"
    
    # SVG Icon
    svg_tag = soup.new_tag('svg', attrs={
        'fill': 'none',
        'height': '14',
        'viewbox': '0 0 15 14',
        'width': '15',
        'xmlns': 'http://www.w3.org/2000/svg'
    })
    path_tag = soup.new_tag('path', attrs={
        'd': 'M13.6875 7.71875C14.0938 7.34375 14.0938 6.6875 13.6875 6.3125L8.6875 1.3125C8.3125 0.90625 7.65625 0.90625 7.28125 1.3125C6.875 1.6875 6.875 2.34375 7.28125 2.71875L10.5625 6H1C0.4375 6 0 6.46875 0 7C0 7.5625 0.4375 8 1 8H10.5625L7.28125 11.3125C6.875 11.6875 6.875 12.3438 7.28125 12.7188C7.65625 13.125 8.3125 13.125 8.6875 12.7188L13.6875 7.71875Z',
        'fill': 'currentcolor'
    })
    svg_tag.append(path_tag)
    
    btn_span.append(" ") # Space
    btn_span.append(svg_tag)
    btn_link.append(btn_span)
    header_btn_div.append(btn_link)
    header_right.append(header_btn_div)
    
    # 2. Header Bar (Mobile Menu)
    header_bar = soup.new_tag('div', attrs={'class': 'it-header-bar d-xl-none text-end'})
    menu_btn = soup.new_tag('button', attrs={'class': 'it-menu-bar'})
    i_tag = soup.new_tag('i', attrs={'class': 'fa-solid fa-bars'})
    menu_btn.append(i_tag)
    header_bar.append(menu_btn)
    
    # Append content to new_col
    new_col.append(header_right)
    new_col.append(header_bar)
    
    # Append new_col to row
    row.append(new_col)
    
    print("Added col-xl-3 (Button) to shop.html")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())

if __name__ == "__main__":
    fix_shop_header()
