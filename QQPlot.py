import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(0)
x = np.random.randn(100)
n, p = 10, .5
s = np.random.binomial(n, p, 1000)
print('random value')
print(x)

plt.figure(figsize=(7,7))
stats.probplot(s, plot=plt)
plt.axis("equal")
plt.show()