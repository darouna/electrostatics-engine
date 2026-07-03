import numpy as np

def make_grid(nx,ny):
    x = np.linspace(0,nx,nx)
    y = np.linspace(0,ny,ny)
    X, Y = np.meshgrid(x,y)
    V = np.zeros_like(X)
    mask = np.zeros_like(X,dtype=bool)
    return X, Y, V, mask