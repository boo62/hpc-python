import numpy as np

a = np.arange(8*8.0).reshape(8, 8)
a_split = np.split(a, 2)
a_2 = np.concatenate(a_split)

print(a)
print(a_split)
print(a_2)


a = np.arange(8*8.0).reshape(8, 8)
a_split = np.split(a, 2, axis=1)
a_2 = np.concatenate(a_split, axis=1)

print(a)
print(a_split)
print(a_2)
