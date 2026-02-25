import numpy as np

a = np.array([[1.8,6.7,1.2],[6.4,1.3,2.7],[2.4,3.5,3.5]],dtype=float)
b = np.array([5.2, 3.8, -0.8])
x = np.linalg.solve(a, b)
print(x)