# We want the following function to median-filter the arrays (as in Problem Set
# 4) but it looks like there is an issue in the plot - the red curve should
# follow the blue points better. What is happening?
# y_new = y is only a reference to y, so you use the values of y and change it
# in y_new[i]. So the results will be false. Also you dont need to copy y. You
# can make an array with the len(x) e.g y_new = np.zeros(len(x)).
import numpy as np
np.random.seed(12345)  # ensures the random values are always the same
import matplotlib.pyplot as plt


def median_filter(x, y, width):
    y_new = np.copy(y)
    for i in range(len(x)):
        y_new[i] = np.median(y[(x > x[i] - width * 0.5) &
                               (x < x[i] + width * 0.5)])
    return y_new

n = 1000
x = np.linspace(0., 100., n)
y = 10. * np.cos(x / 10.) + np.random.normal(0., 5., n)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, '.')
ax.plot(x, median_filter(x, y, 5), color='red', lw=3)
fig.savefig('example_4.png')
