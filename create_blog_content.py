import os
from bs4 import BeautifulSoup
import datetime

# Articles Data
articles = [
    {
        "title": "STEAM: Kunci Melahirkan Generasi Kreatif, Kritis, dan Inovatif",
        "filename": "steam-kunci-generasi-kreatif.html",
        "date": "24 December, 2025",
        "content": """
        <p>Di era perubahan yang begitu cepat, pendidikan tidak lagi cukup hanya berfokus pada hafalan dan nilai akademik semata. Dunia masa depan membutuhkan generasi yang mampu berpikir kritis, kreatif, adaptif, dan mampu menciptakan solusi nyata bagi permasalahan di sekitarnya. Di sinilah pendekatan STEAM (Science, Technology, Engineering, Art, and Mathematics) memegang peran penting.</p>
        <p>STEAM bukan sekadar penggabungan lima disiplin ilmu, melainkan sebuah pendekatan pembelajaran terpadu yang mendorong anak untuk memahami konsep, menghubungkannya dengan dunia nyata, dan mengekspresikannya melalui ide serta karya.</p>
        
        <h4>Mengapa STEAM Relevan untuk Masa Depan Anak?</h4>
        <p>Pendekatan STEAM membantu anak belajar dengan cara yang lebih alami dan kontekstual. Anak tidak hanya belajar “apa”, tetapi juga “mengapa” dan “bagaimana”.</p>
        <p>Melalui STEAM, anak dibiasakan untuk:</p>
        <ul>
            <li>🔍 Menganalisis masalah dan mencari solusi secara logis</li>
            <li>💡 Berpikir kreatif dalam merancang ide dan karya</li>
            <li>🛠️ Membangun dan menguji hasil pemikirannya</li>
            <li>🤝 Berkolaborasi dan berkomunikasi dengan percaya diri</li>
        </ul>
        <p>Kemampuan inilah yang menjadi fondasi keterampilan abad 21, yang sangat dibutuhkan di dunia pendidikan lanjutan maupun dunia kerja masa depan.</p>

        <h4>Peran Setiap Elemen STEAM</h4>
        <ul>
            <li><strong>Science</strong> mengajarkan anak memahami alam dan fenomena di sekitarnya.</li>
            <li><strong>Technology</strong> membekali anak dengan literasi digital dan pemanfaatan teknologi secara bijak.</li>
            <li><strong>Engineering</strong> melatih anak berpikir sistematis, merancang, dan menyelesaikan masalah.</li>
            <li><strong>Art</strong> menumbuhkan kreativitas, empati, dan kemampuan mengekspresikan ide.</li>
            <li><strong>Mathematics</strong> mengasah logika, ketelitian, dan kemampuan berpikir terstruktur.</li>
        </ul>
        <p>Ketika kelima elemen ini dipadukan, anak tidak hanya menjadi pengguna teknologi, tetapi pencipta solusi dan inovasi.</p>

        <h4>STEAM di NanoRobotic: Belajar dengan Proyek Nyata</h4>
        <p>Di NanoRobotic, STEAM diterapkan melalui pembelajaran berbasis proyek (project-based learning). Anak-anak belajar robotik, coding, IoT, dan teknologi digital bukan secara teoritis, tetapi melalui praktik langsung.</p>
        <p>Mereka diajak untuk:</p>
        <ul>
            <li>Merancang dan membuat karya teknologi sederhana</li>
            <li>Menguji ide dan memperbaikinya</li>
            <li>Menjelaskan hasil karyanya dengan bahasa mereka sendiri</li>
            <li>Memahami bahwa teknologi harus memberi manfaat bagi manusia dan lingkungan (Technology for Humanity)</li>
        </ul>
        <p>Pendekatan ini terbukti membantu anak membangun kepercayaan diri, daya pikir kritis, dan kreativitas, sekaligus menumbuhkan kepedulian terhadap isu nyata di sekitarnya.</p>

        <h4>Membangun Generasi Inovator Sejak Dini</h4>
        <p>STEAM bukan tentang mencetak anak menjadi ahli teknologi semata, melainkan membentuk manusia pembelajar sepanjang hayat—anak-anak yang berani mencoba, tidak takut gagal, dan mampu beradaptasi dengan perubahan.</p>
        <p>Melalui STEAM, kita sedang menyiapkan generasi yang:</p>
        <ul>
            <li>Siap menghadapi tantangan masa depan</li>
            <li>Mampu berpikir lintas disiplin</li>
            <li>Memiliki karakter kuat dan nilai kemanusiaan</li>
        </ul>
        <p>Di NanoRobotic, kami percaya bahwa masa depan tidak hanya diwarisi, tetapi dirancang—dan pendidikan STEAM adalah salah satu kuncinya.</p>
        <p>✨ Mari bersama membangun ekosistem belajar yang relevan, bermakna, dan berorientasi masa depan.</p>
        <p>✨ Karena generasi kreatif, kritis, dan inovatif lahir dari pendidikan yang tepat sejak dini.</p>
        """
    },
    {
        "title": "Menjadi Orang Tua Bijak di Era Digital",
        "filename": "menjadi-orang-tua-bijak.html",
        "date": "24 December, 2025",
        "content": """
        <p>Perkembangan teknologi digital telah mengubah cara anak-anak belajar, bermain, dan berinteraksi dengan dunia. Gawai, internet, dan kecerdasan buatan kini menjadi bagian dari keseharian mereka. Di tengah perubahan ini, peran orang tua menjadi semakin penting—bukan untuk menjauhkan anak dari teknologi, tetapi untuk mendampingi, mengarahkan, dan membekali mereka agar bijak menggunakannya.</p>
        <p>Menjadi orang tua di era digital bukanlah tentang melarang, melainkan mendidik dan menyiapkan anak agar mampu tumbuh aman, cerdas, dan berkarakter di tengah arus teknologi yang begitu cepat.</p>

        <h4>Tantangan Orang Tua di Era Digital</h4>
        <p>Anak-anak saat ini tumbuh sebagai digital native. Mereka cepat beradaptasi dengan teknologi, namun belum tentu memahami dampak dan risikonya. Beberapa tantangan yang sering dihadapi orang tua antara lain:</p>
        <ul>
            <li>Paparan konten yang tidak sesuai usia</li>
            <li>Ketergantungan pada gawai</li>
            <li>Minimnya interaksi sosial langsung</li>
            <li>Kurangnya kemampuan berpikir kritis terhadap informasi digital</li>
        </ul>
        <p>Tanpa pendampingan yang tepat, teknologi yang seharusnya menjadi alat belajar justru bisa menjadi penghambat perkembangan anak.</p>

        <h4>Orang Tua Bijak: Pendamping, Bukan Pengawas Semata</h4>
        <p>Orang tua bijak di era digital berperan sebagai pendamping aktif. Artinya, orang tua:</p>
        <ul>
            <li>Mengenal dunia digital yang digunakan anak</li>
            <li>Terlibat dalam aktivitas belajar dan eksplorasi anak</li>
            <li>Menjadi contoh dalam penggunaan teknologi yang sehat</li>
        </ul>
        <p>Dengan pendekatan ini, anak merasa didukung, bukan dikontrol, sehingga lebih terbuka untuk berdiskusi dan belajar bersama.</p>

        <h4>Mengarahkan Anak dari Konsumen Menjadi Kreator</h4>
        <p>Salah satu kunci penting dalam pengasuhan digital adalah membantu anak beralih dari sekadar pengguna teknologi menjadi pencipta dan pemecah masalah. Anak perlu diajak untuk:</p>
        <ul>
            <li>Memahami cara kerja teknologi</li>
            <li>Berpikir kritis dan logis</li>
            <li>Mengembangkan kreativitas melalui proyek nyata</li>
            <li>Menggunakan teknologi untuk memberi manfaat bagi lingkungan dan sesama</li>
        </ul>
        <p>Inilah alasan mengapa pembelajaran berbasis STEM dan STEAM menjadi sangat relevan. Anak tidak hanya bermain dengan teknologi, tetapi belajar menciptakan solusi melalui robotik, coding, dan inovasi digital.</p>

        <h4>Menanamkan Nilai dan Etika Sejak Dini</h4>
        <p>Teknologi yang canggih harus dibarengi dengan nilai yang kuat. Orang tua berperan penting dalam menanamkan:</p>
        <ul>
            <li>Etika digital dan tanggung jawab</li>
            <li>Empati dan kepedulian sosial</li>
            <li>Kesadaran bahwa teknologi harus digunakan untuk kebaikan</li>
        </ul>
        <p>Anak yang dibekali nilai ini akan tumbuh menjadi individu yang tidak hanya cerdas secara teknis, tetapi juga bijak secara moral.</p>

        <h4>Kolaborasi Orang Tua dan Lembaga Pendidikan</h4>
        <p>Pendidikan anak di era digital tidak bisa berjalan sendiri. Diperlukan kolaborasi antara orang tua, sekolah, dan lembaga edukasi yang memiliki visi masa depan. Lingkungan belajar yang tepat akan membantu anak:</p>
        <ul>
            <li>Mengembangkan keterampilan abad 21</li>
            <li>Membangun kepercayaan diri dan karakter</li>
            <li>Siap menghadapi tantangan masa depan yang terus berubah</li>
        </ul>
        <p>Di NanoRobotic, kami percaya bahwa teknologi adalah alat untuk membangun manusia yang lebih baik—Technology for Humanity. Dengan pendampingan orang tua yang bijak dan pendidikan yang tepat, anak-anak dapat tumbuh menjadi generasi yang kreatif, kritis, dan bertanggung jawab.</p>
        <p>✨ Menjadi orang tua bijak di era digital bukan tentang membatasi langkah anak, tetapi tentang menyiapkan mereka agar mampu melangkah dengan arah yang benar.</p>
        <p>✨ Karena masa depan anak tidak hanya ditentukan oleh teknologi yang mereka gunakan, tetapi oleh nilai dan bimbingan yang mereka terima hari ini.</p>
        """
    },
    {
        "title": "Mempersiapkan Generasi Future-Ready: Peran Pendidikan Teknologi Sejak Dini",
        "filename": "mempersiapkan-generasi-future-ready.html",
        "date": "24 December, 2025",
        "content": """
        <p>Dunia terus bergerak dengan kecepatan yang belum pernah terjadi sebelumnya. Perkembangan teknologi seperti kecerdasan buatan, Internet of Things, dan otomatisasi tidak hanya mengubah cara kita bekerja, tetapi juga cara manusia belajar, berpikir, dan berinteraksi. Di tengah perubahan ini, satu hal menjadi semakin jelas: masa depan membutuhkan generasi yang siap beradaptasi, berpikir kritis, dan mampu menciptakan solusi, bukan sekadar mengikuti perubahan.</p>
        <p>Inilah makna dari future-ready generation—generasi yang memiliki kesiapan keterampilan, karakter, dan pola pikir untuk menghadapi dunia yang terus berkembang.</p>

        <h4>Mengapa Pendidikan Teknologi Perlu Dimulai Sejak Dini?</h4>
        <p>Anak-anak saat ini tumbuh di lingkungan digital. Namun, kedekatan dengan teknologi tidak selalu berarti pemahaman yang mendalam. Tanpa arahan yang tepat, anak berisiko menjadi pengguna pasif teknologi.</p>
        <p>Pendidikan teknologi sejak dini membantu anak:</p>
        <ul>
            <li>Memahami cara kerja teknologi, bukan hanya menggunakannya</li>
            <li>Mengembangkan logika, kreativitas, dan rasa ingin tahu</li>
            <li>Melatih problem solving melalui eksperimen dan proyek nyata</li>
            <li>Menumbuhkan kepercayaan diri dalam menghadapi tantangan baru</li>
        </ul>
        <p>Pendekatan ini membuat anak lebih siap menghadapi perubahan, bukan terkejut olehnya.</p>

        <h4>Teknologi sebagai Sarana Membangun Pola Pikir</h4>
        <p>Lebih dari sekadar keterampilan teknis, pendidikan teknologi membentuk pola pikir (mindset). Anak belajar bahwa kegagalan adalah bagian dari proses, kesalahan adalah peluang belajar, dan solusi bisa diciptakan melalui kolaborasi.</p>
        <p>Melalui pembelajaran robotik, coding, dan teknologi digital, anak terbiasa:</p>
        <ul>
            <li>Berpikir sistematis dan terstruktur</li>
            <li>Menghubungkan ide dengan realitas</li>
            <li>Mencoba, mengevaluasi, dan memperbaiki</li>
        </ul>
        <p>Inilah fondasi penting bagi pola pikir inovatif yang dibutuhkan di masa depan.</p>

        <h4>Keterampilan Abad 21 sebagai Pilar Generasi Future-Ready</h4>
        <p>Pendidikan teknologi yang tepat menumbuhkan keterampilan abad 21 yang esensial, antara lain:</p>
        <ul>
            <li>Critical thinking untuk menganalisis masalah</li>
            <li>Creativity untuk menciptakan ide dan solusi</li>
            <li>Collaboration dalam kerja tim</li>
            <li>Communication untuk menyampaikan gagasan dengan percaya diri</li>
        </ul>
        <p>Keterampilan ini tidak hanya relevan untuk dunia kerja, tetapi juga untuk kehidupan sehari-hari dan pembentukan karakter anak.</p>

        <h4>Kolaborasi Orang Tua, Sekolah, dan Ekosistem Edukasi</h4>
        <p>Mempersiapkan generasi future-ready bukanlah tugas satu pihak. Dibutuhkan kolaborasi antara orang tua, sekolah, dan lembaga pendidikan yang memiliki visi jangka panjang. Lingkungan belajar yang suportif dan relevan akan membantu anak tumbuh menjadi pembelajar sepanjang hayat.</p>
        <p>Peran orang tua sebagai pendamping, serta institusi pendidikan sebagai fasilitator pembelajaran bermakna, menjadi kunci dalam menciptakan ekosistem belajar yang sehat dan berkelanjutan.</p>

        <h4>NanoRobotic: Menyiapkan Anak untuk Masa Depan</h4>
        <p>Di NanoRobotic, pendidikan teknologi dirancang sebagai pengalaman belajar yang menyenangkan, terstruktur, dan bermakna. Anak tidak hanya belajar robotik dan coding, tetapi juga memahami bahwa teknologi harus memberi dampak positif bagi manusia dan lingkungan—sejalan dengan nilai Technology for Humanity.</p>
        <p>Kami percaya bahwa masa depan bukan sekadar sesuatu yang dinanti, melainkan sesuatu yang perlu dipersiapkan sejak hari ini. Dengan pendidikan teknologi yang tepat sejak dini, anak-anak Indonesia dapat tumbuh menjadi generasi yang siap menghadapi masa depan dengan percaya diri, kreativitas, dan kepedulian.</p>
        <p>✨ Karena generasi future-ready tidak lahir secara kebetulan, tetapi dibentuk melalui pendidikan yang relevan, visioner, dan berorientasi masa depan.</p>
        """
    }
]

def create_blog_pages():
    try:
        # Load Template
        with open('blog-details.html', 'r', encoding='utf-8') as f:
            template_content = f.read()
        
        template_soup = BeautifulSoup(template_content, 'html.parser')
        
        for article in articles:
            soup = BeautifulSoup(template_content, 'html.parser') # Fresh copy
            
            # Update Page Title
            page_title = soup.find('title')
            if page_title:
                page_title.string = article['title'] + " - kiden"
            
            # Update Post Title
            post_title = soup.find('h4', class_='postbox__title')
            if post_title:
                if post_title.find('a'):
                    post_title.find('a').string = article['title']
                    post_title.find('a')['href'] = '#'
                else:
                    post_title.string = article['title']
            
            # Update Date
            meta_date = soup.find('div', class_='postbox__meta')
            if meta_date:
                span_tags = meta_date.find_all('span')
                if len(span_tags) > 0:
                    # Assuming first span is date from icon
                    # <i class="fa-solid fa-calendar-days"></i> 14 June 2023
                    # We rebuild the span
                    icon = soup.new_tag('i', attrs={'class': 'fa-solid fa-calendar-days'})
                    span_tags[0].clear()
                    span_tags[0].append(icon)
                    span_tags[0].append(f" {article['date']}")

            # Update Content
            # Find the paragraphs
            content_div = soup.find('div', class_='postbox__details-title-box')
            if content_div:
                # Remove existing paragraphs
                for p in content_div.find_all('p'):
                    p.decompose()
                
                # Append new content
                content_soup = BeautifulSoup(article['content'], 'html.parser')
                
                # Add styling to UL tags
                for ul in content_soup.find_all('ul'):
                    ul['style'] = "padding-left: 20px; list-style-type: disc; margin-bottom: 20px;"
                
                content_div.append(content_soup)

            # Remove (Clean up) the "Latest News" section at the bottom
            latest_news_section = soup.find('div', class_='it-blog-area')
            if latest_news_section:
                latest_news_section.decompose()
                print(f"  Removed 'Latest News' section from {article['filename']}")

            # Modify Breadcrumb section
            breadcrumb_section = soup.find('div', class_='it-breadcrumb-area')
            if breadcrumb_section:
                # Change "Blog Details" main heading to Article Title
                breadcrumb_title = breadcrumb_section.find('h3', class_='it-breadcrumb-title')
                if breadcrumb_title:
                    breadcrumb_title.string = article['title']
                
                # Remove "Home // Blog Details" navigation list
                breadcrumb_list = breadcrumb_section.find('div', class_='it-breadcrumb-list')
                if breadcrumb_list:
                    breadcrumb_list.decompose()
                
                print(f"  Updated 'Breadcrumb' title and removed list for {article['filename']}")
            
            # Save file
            with open(article['filename'], 'w', encoding='utf-8') as f_out:
                f_out.write(soup.prettify())
            print(f"Created {article['filename']}")

    except Exception as e:
        print(f"Error creating pages: {e}")

def update_blog_listing():
    try:
        with open('blog.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Find blog items
        # .it-blog-item
        blog_items = soup.find_all('div', class_='it-blog-item')
        
        print(f"Found {len(blog_items)} blog items in blog.html")
        
        for i, article in enumerate(articles):
            if i < len(blog_items):
                item = blog_items[i]
                
                # Update Title
                title_tag = item.find('h4', class_='it-blog-title')
                if title_tag and title_tag.find('a'):
                    title_tag.find('a').string = article['title']
                    title_tag.find('a')['href'] = article['filename']
                
                # Update Date
                meta_div = item.find('div', class_='it-blog-meta')
                if meta_div and meta_div.find('span'):
                    meta_div.find('span').string = article['date']
                
                # Update Image Link (keep image src but change href)
                thumb_div = item.find('div', class_='it-blog-thumb')
                if thumb_div and thumb_div.find('a'):
                    thumb_div.find('a')['href'] = article['filename']
                
                # Update Button Link
                btn_div = item.find('div', class_='it-blog-button')
                if btn_div and btn_div.find('a'):
                    btn_div.find('a')['href'] = article['filename']
                    
                print(f"Updated Item {i+1}: {article['title']}")
            
        # Remove any remaining items (placeholders)
        # We start from index len(articles) up to len(blog_items)
        if len(blog_items) > len(articles):
            print(f"Removing {len(blog_items) - len(articles)} unused placeholders...")
            # We need to act on the soup elements. 
            # Note: decomposing elements while iterating might be tricky if we use the list we just created.
            # But blog_items list holds references to the soup tags.
            
            for i in range(len(articles), len(blog_items)):
                item = blog_items[i]
                # Find wrapper and col
                item_wrap = item.find_parent('div', class_='it-blog-item-wrap')
                if item_wrap:
                    col_div = item_wrap.find_parent('div', class_=lambda x: x and 'col-' in x)
                    if col_div:
                        col_div.decompose()
                        print(f"Removed unused blog item {i+1}")
        
        with open('blog.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print("Updated blog.html")

    except Exception as e:
        print(f"Error updating listing: {e}")

if __name__ == "__main__":
    create_blog_pages()
    update_blog_listing()
