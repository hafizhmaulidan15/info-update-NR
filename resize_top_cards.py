from bs4 import BeautifulSoup

def resize_top_cards():
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
    
    # 1. Update the top row (static cards)
    # The first row contains the Top 3 Static Cards.
    # We want to change col-xl-4 to col-xl-3 and add justify-content-center to the row.
    
    rows = container.find_all('div', class_='row', recursive=False)
    if not rows:
        print("No rows found in container")
        return
        
    top_row = rows[0]
    
    # Add 'justify-content-center' to row if not present
    if 'justify-content-center' not in top_row['class']:
        top_row['class'].append('justify-content-center')
        
    # Find columns in this row
    cols = top_row.find_all('div', class_='col-xl-4')
    
    if not cols:
         # maybe already changed? or used different class?
         cols = top_row.find_all('div', class_='mb-30') # broader search if needed, but let's trust class structure
    
    count = 0
    for col in cols:
        # Check if it is one of the top cards (it-team-2-item inside)
        if col.find('div', class_='it-team-2-item'):
            # Change col-xl-4 to col-xl-3
            # Remove 'col-xl-4', add 'col-xl-3'
            if 'col-xl-4' in col['class']:
                col['class'].remove('col-xl-4')
                col['class'].append('col-xl-3')
                # Optional: Ensure responsiveness? 
                # keep col-lg-6 col-md-6? Or scale them down too?
                # User said "3 kotak atas agak diperkecil" -> implies general size reduction.
                # Changing col-xl-4 (33%) to col-xl-3 (25%) makes them smaller on desktop.
                count += 1
                
    print(f"Resized {count} top partner cards to col-xl-3.")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())

if __name__ == "__main__":
    resize_top_cards()
