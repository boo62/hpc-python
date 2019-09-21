import numpy as np
import matplotlib.pyplot as plt
import pickle

points = np.genfromtxt("points_circle.dat")
vec = np.array((1.2, 1.1)).reshape(-1, 2)

points2 = points + vec

plt.plot(points[:,0], points[:,1], "o")
plt.plot(points2[:,0], points2[:,1], "o")
plt.show()
plt.close()
