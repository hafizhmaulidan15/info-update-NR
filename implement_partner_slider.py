from bs4 import BeautifulSoup

def implement_slider():
    file_path = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\teacher.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # helper to find the main container
    team_area = soup.find('div', class_='it-team-2-area')
    if not team_area:
        print("Could not find it-team-2-area")
        return

    container = team_area.find('div', class_='container')
    row = container.find('div', class_='row')
    
    # Find all columns (cards)
    cols = row.find_all('div', class_='col-xl-4', recursive=False)
    
    if len(cols) < 6:
        print(f"Found {len(cols)} columns. Expected at least 6 to split 3/3.")
        # proceed anyway if we have enough to split at least 1? 
        # User said "3 kotak dibawah", assuming existing content.
        # If fewer, valid logic needed.
    
    # Split: Top 3 stay, Rest go to slider
    static_cards = cols[:3]
    slider_cards = cols[3:]
    
    print(f"Splitting: {len(static_cards)} static, {len(slider_cards)} slider.")
    
    # Create Slider Structure
    # <div class="row mt-60">
    #   <div class="col-xl-12">
    #     <div class="it-team-2-active swiper-container">
    #       <div class="swiper-wrapper">
    #         ... slides ...
    #       </div>
    #     </div>
    #     <div class="it-team-dots text-center mt-60"></div>
    #   </div>
    # </div>
    
    slider_row = soup.new_tag('div', attrs={'class': 'row mt-60'})
    slider_col = soup.new_tag('div', attrs={'class': 'col-xl-12'})
    swiper_container = soup.new_tag('div', attrs={'class': 'it-team-2-active swiper-container'})
    swiper_wrapper = soup.new_tag('div', attrs={'class': 'swiper-wrapper'})
    
    for col in slider_cards:
        # Extract the inner item content
        item_content = col.find('div', class_='it-team-2-item')
        if item_content:
            # Create swiper slide
            slide = soup.new_tag('div', attrs={'class': 'swiper-slide'})
            slide.append(item_content) # Move the item into the slide
            swiper_wrapper.append(slide)
            
            # Remove the original col from the DOM
            col.decompose()
            
    swiper_container.append(swiper_wrapper)
    slider_col.append(swiper_container)
    
    # Pagination/Dots
    dots = soup.new_tag('div', attrs={'class': 'it-team-dots text-center mt-60'})
    slider_col.append(dots)
    
    slider_row.append(slider_col)
    
    # Append the new slider row to the container (after the existing row)
    container.append(slider_row)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())
        print("Slider implemented successfully.")

if __name__ == "__main__":
    implement_slider()
