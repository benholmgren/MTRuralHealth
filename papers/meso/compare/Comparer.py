import numpy as np
from sklearn.neighbors import KernelDensity
from util import calc_linear_frechet

class Comparer:

    def __init__(self, filtration1, filtration2):
        self.filtration1 = filtration1
        self.filtration2 = filtration2

    def calculateKDEdistance(self):
        kde1 = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(self.filtration1)
        kde2 = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(self.filtration2)
        density1 = kde1.score_samples(self.filtration1)
        density2 = kde2.score_samples(self.filtration2)

        disc1 = []
        disc2 = []
        # init proper dimensional vectors
        for i in range(len(self.filtration1)):
            disc1.append([self.filtration1[i][0], density1[i]])

        for j in range(len(self.filtration2)):
            disc2.append([self.filtration2[j][0], density2[j]])

        # print(disc1)
        # print(disc2)
        return calc_linear_frechet(np.array(disc1), np.array(disc2))