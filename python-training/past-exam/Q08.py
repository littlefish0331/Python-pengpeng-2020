import numpy as np

np1 = np.array([6, 5, 4, 3, 2, 1])
np2 = np1.reshape(3, 2)
print(np2.sum(axis = 1))
