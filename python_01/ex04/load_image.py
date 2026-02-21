import matplotlib.pyplot as plt
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Loads the image using mpimg.iread, cuts a square
from it and prints the shape of the image and returns img."""
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise TypeError("Error: unsupported file format")
        img = plt.imread(path)
        print("The shape of the old image is:", img.shape)
        print("the image:", img)
        gray = np.mean(img, axis=2).astype(np.uint8)
        new_img = gray[100:500, 450:850, np.newaxis]
        print("The shape of the image is:", new_img.shape)
        return (new_img)
    except Exception as e:
        print("Error:", e)
        return []
