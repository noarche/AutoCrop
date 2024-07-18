from PIL import Image, ImageEnhance, ImageOps
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def crop_logo(image_path):
    """Function to crop logo images"""
    img = Image.open(image_path)
    img_gray = img.convert('L')
    
    # Invert the grayscale image
    inverted_image = ImageOps.invert(img_gray)
    
    # Find the bounding box of the non-zero regions in the image
    bbox = inverted_image.getbbox()
    
    if bbox:
        # Crop the image using the calculated bounding box
        new_img = img.crop(bbox)
        return new_img
    else:
        # If no bounding box found, return the original image
        return img

def process_images(input_dir):
    supported_formats = ('.png', '.webp')
    processed_count = 0
    for file in os.listdir(input_dir):
        if file.lower().endswith(supported_formats):
            image_path = os.path.join(input_dir, file)
            temp_path = os.path.join(input_dir, f"_{file}")
            cropped_image = crop_logo(image_path)
            cropped_image.save(temp_path, format=file.split('.')[-1].upper())
            os.remove(image_path)
            os.rename(temp_path, image_path)
            print(f"Processed {file}")
            processed_count += 1
    return processed_count

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    input_dir = filedialog.askdirectory(title="Select Input Directory")
    
    if not input_dir:
        messagebox.showerror("Error", "No directory selected.")
        return 0
    
    return process_images(input_dir)

def main():
    while True:
        processed_count = select_directory()
        if processed_count > 0:
            print(f"Total files processed: {processed_count}")
            messagebox.showinfo("Success", f"Total files processed: {processed_count}")
        else:
            print("No files processed.")
        
        run_again = messagebox.askyesno("Run Again", "Do you want to process another directory?")
        if not run_again:
            break

if __name__ == "__main__":
    main()
