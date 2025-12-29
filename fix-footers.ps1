# PowerShell script to fix footers in HTML files
# This script replaces the old default footer content with the correct NANOROBOTIC footer

$projectPath = "d:\Hafizh\Matra\Web Nanorobotic\Template cobaan\kiden"

# List of files that need footer fixes (have 736 University Drive Chicago)
$filesToFix = @(
    "menjadi-orang-tua-bijak.html",
    "steam-kunci-generasi-kreatif.html",
    "404.html",
    "blog-details.html",
    "blog-sidebar.html",
    "cart.html",
    "checkout.html",
    "faq.html",
    "gallery.html",
    "instructor-registration.html",
    "login.html",
    "price.html",
    "program-details.html",
    "register.html",
    "shop-details.html",
    "student-registration.html",
    "teacher-2.html",
    "teacher-details.html",
    "outline web\404.html",
    "outline web\faq.html",
    "outline web\gallery.html"
)

# Define replacements
$replacements = @{
    # Logo area - fix href
    'href="index-html"' = 'href="index.html"'
    
    # Footer text
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt' = 'Untuk mendapatkan berita terbaru tentang Kami, dapat mengakses media sosial kami'
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt\s+ut' = 'Untuk mendapatkan berita terbaru tentang Kami, dapat mengakses media sosial kami'
    
    # Social links
    '<i class="fab fa-facebook-f">' = '<i class="fab fa-instagram">'
    '<i class="fab fa-skype">' = '<i class="fab fa-youtube">'
    '<i class="fab fa-twitter">' = '<i class="fab fa-tiktok">'
    
    # Quick Links menu items
    '>Home<' = '>Beranda<'
    '>About<' = '>Tentang Kami<'
    '>Pages<' = '>Kelas<'
    '>Shop<' = '>Retail<'
    '>Admission<' = '>Artikel<'
    '>Location<' = '>Lokasi<'
    
    # Support section
    '>Contact Us<' = '>Kontak Kami<'
    '>Ticket<' = ''
    '>Parent Community<' = ''
    '>Day Care<' = ''
    
    # Get In Touch - Address
    '736 University Drive Chicago' = 'Jl. Cempaka Blok Z3 No. 1, Taman Cimanggu, Tanah Sereal Kota Bogor, Bogor 16164 Jawa'
    'IL 60606 USA' = 'Barat – Indonesia'
    
    # Phone
    '(+981)312-775-6689' = '0877-9000-5689'
    'tel:+9813127756689' = 'https://api.whatsapp.com/send/?phone=6287790005689&amp;text&amp;type=phone_number&amp;app_absent=0'
    
    # Email
    'brand@gmail.com' = 'nano.idrobotic@gmail.com'
    'mailto:brand@gmail.com' = 'mailto:nano.idrobotic@gmail.com'
    
    # Copyright
    'NanoRoboticTemplate' = 'Nanorobotic'
    
    # Social media links
    '<a href="#">\s*<i class="fab fa-instagram">' = '<a href="https://www.instagram.com/nano_robotic?utm_source=qr&amp;igsh=MTQ2ZW1nd3BkZGs5YQ=="><i class="fab fa-instagram">'
    '<a href="#">\s*<i class="fab fa-youtube">' = '<a href="https://youtube.com/@nanorobotic470?si=ywGjojMn23cnjaM5"><i class="fab fa-youtube">'
    '<a href="#">\s*<i class="fab fa-tiktok">' = '<a href="https://www.tiktok.com/@nano_robotic"><i class="fab fa-tiktok">'
}

Write-Host "Starting footer fix process..."
Write-Host "Found $($filesToFix.Count) files to process."

foreach ($file in $filesToFix) {
    $filePath = Join-Path $projectPath $file
    if (Test-Path $filePath) {
        Write-Host "Processing: $file"
        $content = Get-Content $filePath -Raw -Encoding UTF8
        
        foreach ($old in $replacements.Keys) {
            $new = $replacements[$old]
            if ($new -eq '') { continue }
            $content = $content -replace [regex]::Escape($old), $new
        }
        
        $content | Set-Content $filePath -Encoding UTF8
        Write-Host "  Fixed: $file"
    } else {
        Write-Host "  NOT FOUND: $file" -ForegroundColor Yellow
    }
}

Write-Host "`nFooter fix process completed!"
