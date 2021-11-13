import numpy as np
import matplotlib.pyplot as plt

def imshow(X, resize=None):
    img = Image.open(X)
    img = np.resize(img,resize)
    fig, ax = plt.subplots()
    ax.imshow(img, cmap='jet', interpolation='nearest')
    plt.show()
