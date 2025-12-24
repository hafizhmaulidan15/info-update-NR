import shutil
import os

def move_upskill_image():
    # Use raw string for source path
    source = r'C:\Users\Hafizh Maulidan\.gemini\antigravity\brain\eba42090-128c-42c5-9749-09ee5346445b\uploaded_image_1766567300778.png'
    
    dest_dir = r'd:\Hafizh\Matra\Web Nanorobotic\Template cobaan\kiden\assets\img\teacher'
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    dest_file = 'upskill_knowledge.png'
    dest_path = os.path.join(dest_dir, dest_file)
    
    try:
        shutil.copy2(source, dest_path)
        print(f"Image copied to {dest_path}")
    except Exception as e:
        print(f"Error copying image: {e}")

if __name__ == "__main__":
    move_upskill_image()
