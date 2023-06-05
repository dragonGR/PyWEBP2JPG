from PIL import Image

def convert_webp_to_jpg(input_file, output_file):
    try:
        # Open the WebP image
        with Image.open(input_file) as img:
            # Convert to RGB mode if the image is in CMYK mode
            if img.mode == 'CMYK':
                img = img.convert('RGB')
            
            # Save as JPG
            img.save(output_file, 'JPEG')
            
        print('Conversion successful!')
        
    except IOError:
        print(f'Unable to open {input_file}')
        
# Example usage
input_image = 'input.webp'
output_image = 'output.jpg'
convert_webp_to_jpg(input_image, output_image)