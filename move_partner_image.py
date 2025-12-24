import shutil
import os

def move_image():
    # Use raw string for source path to avoid escape issues, and normalized path
    source = r'C:\Users\Hafizh Maulidan\.gemini\antigravity\brain\eba42090-128c-42c5-9749-09ee5346445b\uploaded_image_1766567212999.png'
    
    # Destination directory structure seems to be assets/img/teacher (from list_dir check)
    # If list_dir fails, we'll know. But let's assume valid based on file view earlier.
    
    dest_dir = r'd:\Hafizh\Matra\Web Nanorobotic\Template cobaan\kiden\assets\img\teacher'
    
    # Create dir if not exists (though it should)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    dest_file = 'partner_cabang.png'
    dest_path = os.path.join(dest_dir, dest_file)
    
    try:
        shutil.copy2(source, dest_path)
        print(f"Image copied to {dest_path}")
    except Exception as e:
        print(f"Error copying image: {e}")

if __name__ == "__main__":
    move_image()
