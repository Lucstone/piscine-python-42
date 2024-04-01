from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
Load an image from a file and return it as an array of pixels.
Args:
path (str): The path to the image file.
Returns:
np.ndarray: An array representing the image pixels.
    """
    try:
        img = Image.open(path)
        img_array = np.array(img)
        return img_array
    except Exception as e:
        print(f"Error: {e}")
        return None


def main():
    return


if __name__ == "__main__":
    main()
