import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def rotate(img: np.ndarray):
    """Takes a image as a parameter and
does transpose it to produce an image"""
    img = img[:, :, 0]
    res = [[img[i][j] for i in range(len(img))] for j in range(len(img[1]))]
    np_change = np.array(res)
    print("New shape after Transpose:", np_change.shape)
    print(np_change)
    plt.imshow(np_change, cmap="gray")
    plt.show()


def main():
    img = ft_load("animal.jpeg")
    print(img)
    rotate(img)


if __name__ == "__main__":
    main()
