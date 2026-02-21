import array
import matplotlib.pyplot as plt


def ft_invert(img) -> array:
    """Inverts the color of the image received."""
    try:
        img_rgb = img.copy()
        new_img = 255 - img_rgb
        plt.title("Invert Image")
        plt.imshow(new_img)
        plt.show()
        return new_img
    except Exception as e:
        print("Error:", e)


def ft_red(img) -> array:
    """Applies red filter to the image received"""
    try:
        img_rgb = img.copy()
        img_rgb[:, :, 2] = 0
        img_rgb[:, :, 1] = 0
        plt.title("Red Image")
        plt.imshow(img_rgb)
        plt.show()
        return (img_rgb)
    except Exception as e:
        print("Error:", e)


def ft_green(img) -> array:
    """Applies green filter to the image received"""
    try:
        img_rgb = img.copy()
        img_rgb[:, :, 2] = 0
        img_rgb[:, :, 0] = 0
        plt.title("Green Image")
        plt.imshow(img_rgb)
        plt.show()
        return (img_rgb)
    except Exception as e:
        print("Error:", e)


def ft_blue(img) -> array:
    """Applies blue filter to the image received"""
    try:
        img_rgb = img.copy()
        img_rgb[:, :, 1] = 0
        img_rgb[:, :, 0] = 0
        plt.title("Blue Image")
        plt.imshow(img_rgb)
        plt.show()
        return (img_rgb)
    except Exception as e:
        print("Error:", e)


def ft_grey(img) -> array:
    """Applies grey filter to the image received"""
    try:
        img_rgb = img.copy()
        grey = img_rgb[:, :, 1]
        plt.title("Grey Image")
        plt.imshow(grey, cmap="grey")
        plt.show()
        return (grey)
    except Exception as e:
        print("Error:", e)
