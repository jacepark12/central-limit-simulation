import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

mu = 2
std = 2
rv = stats.norm(mu, std)


xx = np.linspace(-5, 5, 100)
plt.plot(xx, rv.pdf(xx))
plt.ylabel("p(x)")
plt.title("pdf of normal distribution")
plt.show()