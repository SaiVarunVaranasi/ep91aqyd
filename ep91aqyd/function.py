import numpy as np
import cv2
import matplotlib.pyplot as plt

def imshow(X, resize=None):
    img = cv2.imread(X)
    img = np.resize(img,resize)
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
