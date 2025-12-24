from bs4 import BeautifulSoup

def refine_shop_layout_v2():
    file_path = 'd:\\Hafizh\\Matra\\Web Nanorobotic\\Template cobaan\\kiden\\shop.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Remove "Sale" badges
    badges = soup.find_all('div', class_='it-shop-badge-item')
    print(f"Found {len(badges)} sale badges. Removing...")
    for badge in badges:
        badge.decompose()
        
    with open(file_path, 'w', encoding='utf-8') as f_out:
        f_out.write(soup.prettify())

if __name__ == "__main__":
    refine_shop_layout_v2()
