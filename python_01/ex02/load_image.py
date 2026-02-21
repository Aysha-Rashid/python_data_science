import array as array
import matplotlib.pyplot as plt


def ft_load(path: str) -> array:
    """Loads the image using mpimg.iread, prints the
shape of the image and returns img."""
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise TypeError("unsupported file format")
        img = plt.imread(path)
        print("The shape of image is:", img.shape)
        return (img)
    except Exception as e:
        print("Error:", e)
        return []
