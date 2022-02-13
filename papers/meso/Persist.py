import math

import dionysus as d
import rpy2 as r
from sklearn.neighbors import KernelDensity
import numpy as np
from sklearn.metrics import DistanceMetric


# Run Vietoris-Rips Filtration on np array
def run_rips(cloud):
    print('Generating filtration for img01')
    # max dimension = 3, max radius = 2
    f = d.fill_rips(cloud, 1, 20)
    p = d.homology_persistence(f)
    dgms = d.init_diagrams(p, f)
    d.plot.plot_diagram(dgms[0], show=True)
    # get rid of pts at infinity to fix distance
    for point in dgms[0]:
        if point.death == math.inf:
            print(point)
            del point
    return dgms

def kde_dist(x, y):
    kde1 = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(x)
    kde2 = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(y)
    density1 = kde1.score_samples(x)
    density2 = kde2.score_samples(y)

    disc1 = []
    disc2 = []
    # init proper dimensional vectors
    for i in range(len(x)):
        disc1.append([x[i][0], density1[i]])

    for j in range(len(y)):
        disc2.append([y[j][0], density2[j]])

    print(disc1)
    print(disc2)
    print(calc_linear_frechet(np.array(disc1), np.array(disc2)))
#    pairs = dist.pairwise(density1, density2)

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

# Don't work! Need a bijection.
def wass_dist(diag1, diag2):
    return d.wasserstein_distance(diag1, diag2)

def bottle_dist(diag1, diag2):
    return d.bottleneck_distance(diag1, diag2)

