from bs4 import BeautifulSoup

def revert_top_cards():
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
    rows = container.find_all('div', class_='row', recursive=False)
    if not rows:
        print("No rows found in container")
        return
        
    top_row = rows[0]
    
    # Remove 'justify-content-center' if present (back to original behavior, usually left aligned or just full row)
    if 'justify-content-center' in top_row.get('class', []):
        top_row['class'].remove('justify-content-center')
        
    # Find columns in this row
    cols = top_row.find_all('div', class_='col-xl-3')
    
    count = 0
    for col in cols:
        # Check if it is one of the top cards (it-team-2-item inside)
        if col.find('div', class_='it-team-2-item'):
            # Change col-xl-3 back to col-xl-4
            col['class'].remove('col-xl-3')
            col['class'].append('col-xl-4')
            count += 1
                
    print(f"Reverted {count} top partner cards to col-xl-4.")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())

if __name__ == "__main__":
    revert_top_cards()
