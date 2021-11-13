import numpy as np
import matplotlib.pyplot as plt

def imshow(X, resize):
    arr = np.load(X)
    img = Image.fromarray(arr)
    img.resize(size=(100, 100))
    fig, ax = plt.subplots()
    ax.imshow(img)
    plt.show()
