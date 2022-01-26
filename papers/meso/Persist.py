import math

import dionysus as d
import rpy2 as r

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




def wass_dist(diag1, diag2):
    return d.wasserstein_distance(diag1, diag2)

def bottle_dist(diag1, diag2):
    return d.bottleneck_distance(diag1, diag2)

