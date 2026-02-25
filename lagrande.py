import numpy as np
from scipy.interpolate import lagrange

x_date = np.array([1, 2, 3])
y_date = np.array([5.2, 3.8, -0.8])

# 使用拉格朗日插值法进行插值
# сетка для графика
x_sm = np.linspace(1, 3, 100)

result = lagrange(x_date, y_date)(x_sm)
print(result)