from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    This function takes a path of image and try to open it,
    if successful print the shape of image and
    return the data (pixels values) of the image
    """

    try:
        image = Image.open(path)
        pixels = np.array(image)

        print(f"The shape of image is: {pixels.shape}")

        return pixels

    except FileNotFoundError:
        print(f"Error: file '{path}' not found")
    except PermissionError:
        print(f"Error: Permission denied for file '{path}'.")
    except OSError as e:
        print(f"Error: Unable to open file '{path}' - {e}")
    return None
