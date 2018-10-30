import math
import numpy as np
from scipy.stats import pearsonr

def calcMean(x,y):
    sum_x = sum(x)
    sum_y = sum(y)
    n = len(x)
    x_mean = float(sum_x+0.0)/n
    y_mean = float(sum_y+0.0)/n
    return x_mean,y_mean

def calcPearson(x,y):
    x_mean,y_mean = calcMean(x,y)
    n = len(x)
    sumTop = 0.0
    sumBottom = 0.0
    x_pow = 0.0
    y_pow = 0.0
    for i in range(n):
        sumTop += (x[i]-x_mean)*(y[i]-y_mean)
    for i in range(n):
        x_pow += math.pow(x[i]-x_mean,2)
    for i in range(n):
        y_pow += math.pow(y[i]-y_mean,2)
    sumBottom = math.sqrt(x_pow*y_pow)
    p = sumTop/sumBottom
    return p

if __name__ == "__main__": 
	# points for table 4 and table 7
	points = [[3.3, 6.5, 2.8, 3.4, 5.5], 
			  [3.5, 5.8, 3.1, 3.6, 5.1], 
			  [5.6, 3.3, 4.5, 5.2, 3.2], 
			  [5.4, 2.8, 4.1, 4.9, 2.8], 
			  [5.2, 3.1, 4.7, 5.3, 3.1]]
	# points for table 9
	points = [[5.4, 2.8, 4.1], 
			  [5.2, 3.1, 4.7], 
			  [3.3, 4.2, 5.2], 
			  [4.1, 3.7, 3.5], 
			  [4.6, 4.0, 4.1]]
	data_size = len(points)
	res = list()
	for i in range(data_size):
		for j in range(i + 1, data_size):
			value = calcPearson(points[i], points[j])
			res.append(value)
	print res