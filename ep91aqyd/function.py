import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt

def imshow(X, resize):
    img = Image.open("image_path.jpg")
    img = np.resize(img, resize)
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
