import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def imshow(X, resize=None):
    img = Image.open(X)
    img = np.resize(X,resize)
    plt.imshow(img)
    plt.show()
    
