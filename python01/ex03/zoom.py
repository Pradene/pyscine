from load_image import ft_load
from PIL import Image
import numpy as np


def zoom(path: str):
    """
    This function try to grayscale and zoom an image loaded with ft_load
    """

    pixels = ft_load(path)

    print(pixels)

    if pixels.ndim == 3 and pixels.shape[2] == 3:
        grayscale_pixels = np.dot(pixels[..., :3], [0.2989, 0.5870, 0.1140])
    elif pixels.ndim == 3 and pixels.shape[2] == 4:
        grayscale_pixels = np.dot(pixels[..., :3], [0.2989, 0.5870, 0.1140])
    elif pixels.ndim == 2:  # Already grayscale
        grayscale_pixels = pixels
    else:
        raise ValueError(
            "Invalid image format. Expected shape: (H, W, 3) or (H, W, 4)"
        )

    pixels = np.round(grayscale_pixels).astype(np.uint8)

    size = 400

    # Compute cropping coordinates (centered)
    start_x = 450
    start_y = 100
    end_x = start_x + size
    end_y = start_y + size

    # Crop the image
    pixels = pixels[start_y:end_y, start_x:end_x]
    print(f"New shape after slicing: {pixels.shape}")
    print(pixels[:, :, np.newaxis])

    image = Image.fromarray(pixels)
    image = image.resize((size, size))

    image.save("assets/zoomed.jpeg", "JPEG")

    return
