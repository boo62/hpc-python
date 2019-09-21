import time
import numpy as np
import matplotlib.pyplot as plt

def finite_difference(y, dx):
    return (y[2:] - y[:-2]) / (2*dx)

if __name__ == "__main__":
    dx = 0.1
    x = np.arange(0, np.pi/2 + 0.01, dx)
    y = np.sin(x)

    res = finite_difference(y, dx)

    mse = np.mean((res - np.cos(x[1:-1]))**2)
    print(mse)
    plt.plot(x[1:-1], res, label="dsin(x)/dx")
    plt.plot(x[1:-1], np.cos(x[1:-1]), label="cos")
    plt.legend()
    plt.show()
