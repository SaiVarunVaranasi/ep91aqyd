import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def imshow(X, resize=None):
    img = Image.open(X)
    img = np.resize(img,resize)
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
