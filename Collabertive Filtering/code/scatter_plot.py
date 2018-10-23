# Chuanxi Zhang
# 10.22.2018

import numpy as np
import matplotlib.pyplot as plt

# the x-axis and y-axis for 5 users
x = np.array([3.3, 5.8, 3.6, 3.4, 5.2])
y = np.array([6.5, 2.6, 6.3, 5.8, 3.1])

color = np.array(['m', 'c', 'r', 'g', 'y'])
data_size = len(x)

# draw graph
figure = plt.figure()
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([0, 7, 0, 7])
for idx in range(data_size):
	username = 'user%s' % (idx + 1)
	plt.scatter(x[idx], y[idx], marker = 'x', color = color[idx], label = username)

plt.legend(loc = 'upper right')
plt.show()
