import os
import cv2
from PIL import Image
import numpy as np

from .path import get_temp_path

def prepare_image():
    img_path = get_temp_path()
    img_file = os.path.join(img_path, "img.png")
    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
    img = cv2.bitwise_not(img)
    res = cv2.resize(img, dsize=(28, 28), interpolation=cv2.INTER_LINEAR)
    res_file = os.path.join(img_path, "res.png")
    cv2.imwrite(res_file, res)
    f = Image.open(res_file)
    img_array = np.asarray(f)
    img_array = img_array.reshape(1, 28, 28)
    img_array = img_array.astype('float32') / 255.0
    print(img_array)
    return img_array