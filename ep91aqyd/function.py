import numpy as np
import matplotlib.pyplot as plt

def imshow(X, resize):
    X = np.resize(X,resize)
    plt.imshow(X)
