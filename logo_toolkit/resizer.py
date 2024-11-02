from PIL import Image
import os

def resize_image(input_path, output_path, size=(150, 150)):
    try:
        with Image.open(input_path) as img:
            img = img.convert("RGBA")  # Ensure it can handle images with transparency
            img.thumbnail(size, Image.LANCZOS)

            # Create a new image with a white background
            new_img = Image.new("RGBA", size, (255, 255, 255, 0))
            new_img.paste(
                img, ((size[0] - img.size[0]) // 2, (size[1] - img.size[1]) // 2)
            )

            # Convert back to RGB if needed (removes alpha)
            new_img = new_img.convert("RGB")
            new_img.save(output_path)

            print(f"Resized image saved at: {output_path}")
    except Exception as e:
        print(f"Error resizing image '{input_path}': {e}")

