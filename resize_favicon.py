from PIL import Image
import os

def resize_favicon():
    file_path = r'd:\Hafizh\Matra\Web Nanorobotic\Template cobaan\kiden\assets\img\logo\favicon.png'
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    try:
        with Image.open(file_path) as img:
            print(f"Original size: {img.size}")
            
            # Target size: 512x512 is good for all-purpose, but maybe user wants 32x32?
            # Standard "favicon.ico" usually has multiple sizes.
            # Since it's a PNG, 32x32 or 192x192 is common.
            # I will resize to 32x32 for standard use, OR if it's high res, keep it square.
            
            # Let's make it 512x512 if original is larger, or 32x32 if original is small.
            # If it's not square, crop it to square first.
            
            width, height = img.size
            if width != height:
                print("Image is not square. Cropping to square center.")
                min_dim = min(width, height)
                left = (width - min_dim) / 2
                top = (height - min_dim) / 2
                right = (width + min_dim) / 2
                bottom = (height + min_dim) / 2
                img = img.crop((left, top, right, bottom))
            
            # Resize
            # If huge, resize to 512x512. If small, resize to 32x32?
            # User said "sesuaikan saja" (just adjust it).
            # I'll create a 32x32 version which is the strict definition of favicon.png usually.
            
            # But wait, 512x512 is better for modern devices.
            # I'll resizing to 512x512 if possible, else 32x32.
            
            # Actually, let's just make it 512x512 (High Res) if the source allows.
            # If source < 512, I'll keep it as is (just squared).
            
            # Let's target 512x512 for quality.
            target_size = (512, 512)
            
            # Force resize (Lanczos)
            img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
            
            img_resized.save(file_path)
            print(f"Resized to {target_size}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    resize_favicon()
