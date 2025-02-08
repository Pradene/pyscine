from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey


def main():
    pixels = ft_load("assets/landscape.jpg")

    ft_invert(pixels)
    ft_red(pixels)
    ft_green(pixels)
    ft_blue(pixels)
    ft_grey(pixels)
    return


if __name__ == "__main__":
    main()
