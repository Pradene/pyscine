import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received
    """

    image = Image.fromarray(255 - array)
    image.show()


def ft_red(array) -> np.ndarray:
    """
    Red scale image received
    """
    pixels = array.copy()
    pixels[:, :, 1] = 0
    pixels[:, :, 2] = 0

    image = Image.fromarray(pixels)
    image.show()


def ft_green(array) -> np.ndarray:
    """
    Green scale image received
    """
    pixels = array.copy()
    pixels[:, :, 0] = 0
    pixels[:, :, 2] = 0

    image = Image.fromarray(pixels)
    image.show()


def ft_blue(array) -> np.ndarray:
    """
    Blue scale image received
    """
    pixels = array.copy()
    pixels[:, :, 0] = 0
    pixels[:, :, 1] = 0

    image = Image.fromarray(pixels)
    image.show()


def ft_grey(array) -> np.ndarray:
    """
    Grey scale image received
    """
    pixels = array.copy()

    red_channel = pixels[:, :, 0] / 3
    green_channel = pixels[:, :, 1] / 3
    blue_channel = pixels[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)

    image = Image.fromarray(grey_image.astype(np.uint8))
    image.show()
