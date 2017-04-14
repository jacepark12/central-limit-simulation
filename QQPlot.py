import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


np.random.seed(0)
x = np.random.randn(100)
plt.figure(figsize=(7,7))
stats.probplot(x, plot=plt)
plt.axis("equal")
plt.show()