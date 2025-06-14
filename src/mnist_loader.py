import gzip
import os
import numpy as np
from .path import get_data_path

def load_train_data(data_path):

    img_path = os.path.join(data_path, "train-images-idx3-ubyte.gz")
    lab_path = os.path.join(data_path, "train-labels-idx1-ubyte.gz")
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Expected MNIST image file not found: {img_path}")
    try:
        with gzip.open(img_path, "rb") as f:
            img_data = f.read()
    except OSError as e:
        raise RuntimeError(f"Error reading MNIST image file: {img_path}") from e
    if not os.path.exists(lab_path):
        raise FileNotFoundError(f"Expected MNIST label file not found: {lab_path}")
    try:
        with gzip.open(lab_path, "rb") as f:
            lab_data = f.read()
    except OSError as e:
        raise RuntimeError(f"Error reading MNIST label file: {lab_path}") from e
    return img_data, lab_data

def load_test_data(data_path):
    img_path = os.path.join(data_path, "t10k-images-idx3-ubyte.gz")
    lab_path = os.path.join(data_path, "t10k-labels-idx1-ubyte.gz")
    if not os.path.exists(img_path):
        raise FileNotFoundError(f"Expected MNIST image file not found: {img_path}")
    try:
        with gzip.open(img_path, "rb") as f:
            img_data = f.read()
    except OSError as e:
        raise RuntimeError(f"Error reading MNIST image file: {img_path}") from e
    if not os.path.exists(lab_path):
        raise FileNotFoundError(f"Expected MNIST label file not found: {lab_path}")
    try:
        with gzip.open(lab_path, "rb") as f:
            lab_data = f.read()
    except OSError as e:
        raise RuntimeError(f"Error reading MNIST label file: {lab_path}") from e
    return img_data, lab_data

def convert_img_data(img_data):
    img_data = img_data[16:] #skips the first 16 bytes of the mnist lavel file as it contains header info
    img_array = np.frombuffer(img_data, dtype=np.uint8)
    num_images = len(img_array) // (28 * 28)
    img_array = img_array.reshape((num_images, 28, 28), order='C')
    return img_array

def convert_lab_data(lab_data):

    lab_data = lab_data[8:] #skips the first 8 bytes of the mnist lavel file as it contains header info
    lab_array = np.frombuffer(lab_data, dtype=np.uint8)
    return lab_array

def plot_img(img_array):
    import matplotlib.pyplot as plt
    import random
    idx = random.randint(0, len(img_array) - 1)  # random index
    random_img = img_array[idx]                  # pick the random image
    plt.imshow(random_img, cmap='gray')
    plt.title(f"MNIST Image (Index: {idx})")
    plt.axis('off')
    plt.show()

def main():

    data_path = get_data_path()
    img_data, lab_data = load_train_data(data_path)
    img_array = convert_img_data(img_data)
    lab_array = convert_lab_data(lab_data)
    plot_img(img_array)

if __name__ == "__main__":
    main()