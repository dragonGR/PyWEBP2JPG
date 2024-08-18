from PIL import Image
import os

def convert_webp_to_jpg(input_file, output_file, quality=85):
    """Converts a WebP image to JPG with quality control and error handling.

    Args:
        input_file (str): Path to the input WebP image.
        output_file (str): Path to the output JPG image.
        quality (int, optional): Quality level for JPG compression (0-95). Defaults to 85.

    Raises:
        FileNotFoundError: If the input file is not found.
        IOError: If there's an error during conversion.
    """

    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

        # Open the WebP image
        with Image.open(input_file) as img:
            # Convert to RGB mode if necessary
            if img.mode == 'CMYK':
                img = img.convert('RGB')

            # Save as JPG with quality control
            img.save(output_file, 'JPEG', quality=quality)

        print(f"Conversion successful! Image saved to: {output_file}")

    except (FileNotFoundError, IOError) as e:
        print(f"Error converting image: {e}")

# Example usage
input_image = 'sample.webp'
output_image = 'sample.jpg'
convert_webp_to_jpg(input_image, output_image)
