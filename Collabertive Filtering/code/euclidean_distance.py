import numpy as np

def calculate_distance(d):
    return ((d ** 2).sum(axis=0)) ** 0.5

def euclidean_distance(point_a, point_b):
    d_value = point_b - point_a
    return calculate_distance(d_value)

def normalization(values):
	min_value = min(values)
	max_value = max(values)
	res = list()
	for value in values:
		value = 1 / (value + 1)
		res.append(value)
	return res

if __name__ == "__main__": 
	x = np.array([3.3, 5.8, 3.6, 3.4, 5.2])
	y = np.array([6.5, 2.6, 6.3, 5.8, 3.1])
	points = np.stack((x, y), axis = -1)
	data_size = len(points)
	res = list()
	for i in range(data_size):
		for j in range(i + 1, data_size):
			value = euclidean_distance(points[i], points[j])
			res.append(value)
	print res
	print normalization(np.array(res))
	



