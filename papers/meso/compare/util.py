import math
import numpy as np

def euclidean_distance(p1, p2):
    dist = math.sqrt(((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))
    return dist

def calc_linear_frechet(p, q):
    p_shape = p.shape[0]
    q_shape = q.shape[0]

    calculations_array = np.zeros((p_shape, q_shape))

    for i in range(p_shape):
        for j in range(q_shape):
            d = euclidean_distance(p[i], q[j])

            if i > 0 and j > 0:
                calculations_array[i, j] = max(min(calculations_array[i - 1, j],
                                                   calculations_array[i - 1, j - 1],
                                                   calculations_array[i, j - 1]), d)
            elif i > 0 and j == 0:
                calculations_array[i, j] = max(calculations_array[i - 1, 0], d)
            elif i == 0 and j > 0:
                calculations_array[i, j] = max(calculations_array[0, j - 1], d)
            elif i == 0 and j == 0:
                calculations_array[i, j] = d
            else:
                calculations_array[i, j] = np.infty

    return calculations_array[(p.shape[0] - 1), (q.shape[0] - 1)]