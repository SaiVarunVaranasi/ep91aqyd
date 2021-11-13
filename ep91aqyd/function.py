import numpy as np
import cv2
import matplotlib.pyplot as plt

def imshow(X, resize):
    img = cv2.imread(X)
    img = cv2.resize(img, dsize=resize, interpolation=cv2.INTER_CUBIC)
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
