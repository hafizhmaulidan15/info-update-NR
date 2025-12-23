import os
import re

root_dir = r"d:\Hafizh\Matra\Web Nanorobotic\Template cobaan\kiden"
new_href = "https://api.whatsapp.com/send/?phone=6287790005689&text&type=phone_number&app_absent=0"

# Regex to find the anchor tag containing "BOOK FREE TRIAL"
# We match:
# 1. <a ... href=" (or ')
# 2. current_url (non-greedy)
# 3. " (or ') ... > ... BOOK FREE TRIAL
# We use [\s\S] to match newlines instead of DOTALL for safer syntax.
regex_str = r'(<a\s+[^>]*href=["\'])([^"\']*?)(["\'][^>]*>[\s\S]*?BOOK FREE TRIAL)'
pattern = re.compile(regex_str, re.IGNORECASE)

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(subdir, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check quickly if potentially relevant
                if "BOOK FREE TRIAL" in content.upper():
                    new_content = pattern.sub(r'\1' + new_href + r'\3', content)
                    
                    if new_content != content:
                        print(f"Updating {filepath}")
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
