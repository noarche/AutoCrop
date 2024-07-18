from PIL import Image, ImageEnhance, ImageOps
import os

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

def main():
    """Main function to get user inputs and process images"""
    input_dir = input("Enter the path to the input directory: ").strip()
    output_dir = input("Enter the path to the output directory: ").strip()

    if not os.path.exists(input_dir):
        print("Input directory does not exist.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in os.listdir(input_dir):
        if file.lower().endswith(".png"):
            image_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            cropped_image = crop_logo(image_path)
            cropped_image.save(output_path)
            print(f"Processed {file}")

if __name__ == "__main__":
    main()
