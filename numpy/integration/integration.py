import numpy as np
import matplotlib.pyplot as plt

def reimann_sum(dx):
    x = np.arange(dx/2, np.pi/2, dx)
    res = np.sum(np.sin(x))*dx
    return res
    # return np.sum((y[:-1] + y[1:])/2)

dxs = np.logspace(-6, -4, 5)
res = []
for dx in dxs:
    res.append(reimann_sum(dx))
res = np.array(res)

plt.semilogx(dxs, res-1)
plt.show()
plt.close()
