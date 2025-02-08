from load_image import ft_load
from PIL import Image
import numpy as np


def rotate(path: str):
    """
    This function try to rotate an image loaded with ft_load
    """

    pixels = ft_load(path)
    print(pixels[:, :, np.newaxis])

    height = len(pixels)
    width = len(pixels[0])

    # Convert pixels to a 2D list
    pixels = list(pixels)

    # Initialize a new 2D list for the rotated pixels
    rotated_pixels = [[0] * height for _ in range(width)]

    # Perform the 90 degree rotation
    for i in range(height):
        for j in range(width):
            rotated_pixels[width - 1 - j][i] = pixels[i][j]

    pixels = np.array(rotated_pixels, dtype=np.uint8)

    print(f"New shape after Transpose is: {pixels.shape}")
    print(pixels)

    image = Image.fromarray(pixels)
    image.save("assets/rotated.jpeg")

    return
