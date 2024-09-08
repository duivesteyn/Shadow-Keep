# py 
# functions for the shadow keep map rendering
# bmd
from PIL import Image
from functools import reduce

#https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))



def create_image_from_ascii(ascii_art, img_map, output_size=(1024, 1024), char_size=(50, 50)):
    """
    Create an image by replacing ASCII characters with corresponding images.
    
    ascii_art: 2D array of characters (ASCII art)
    img_map: Dictionary mapping characters to image file paths
    output_size: Size of the final image (width, height)
    char_size: Size for each character-replacing image (width, height)
    """
    # Calculate final image size based on character size and ASCII dimensions
    ascii_height = len(ascii_art)
    ascii_width = len(ascii_art[0]) if ascii_height > 0 else 0
    
    final_image_width = ascii_width * char_size[0]
    final_image_height = ascii_height * char_size[1]
    
    final_image = Image.new("RGB", (final_image_width, final_image_height))

    # Iterate through each character in the ASCII art and paste corresponding image
    for i, row in enumerate(ascii_art):
        for j, char in enumerate(row):
            if char in img_map:
                # Open the image corresponding to the current ASCII character
                img = Image.open(img_map[char])
                
                # Resize the image to the specified character size
                img = img.resize(char_size)
                
                # Calculate the position to paste the image
                pos_x = j * char_size[0]
                pos_y = i * char_size[1]
                
                # Paste the image into the final image
                final_image.paste(img, (pos_x, pos_y))

    # Resize the final image to the desired output size
    final_image = final_image.resize(output_size)
    
    return final_image