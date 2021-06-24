import numpy as np
import matplotlib.pyplot as plt


# general params
interval = [-5, 5]
nb_points = 100

# data
x = np.linspace(*interval, nb_points)
func = lambda u: u ** 2

plt.plot(x, func(x))
plt.show()
