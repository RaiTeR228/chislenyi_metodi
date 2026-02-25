import numpy as np

# Исправлено: все списки объединены в один список списков
# Исправлено: dtype (было dype)
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

b = np.array([8, -11, -3], dtype=float)
x_numpy = np.linalg.solve(A, b)

for i, val in enumerate(x_numpy):
    print(f"x{i+1} = {val}")