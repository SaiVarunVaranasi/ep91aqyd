import numpy as np
import matplotlib.pyplot as plt

def imshow(X, resize):
    file = open(X, "r")
    img = np.load(file)
    file.close()
    img = np.resize(img, resize)
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
