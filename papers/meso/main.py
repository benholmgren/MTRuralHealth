import numpy as np
from compare.Comparer import Comparer

if __name__ == '__main__':
    path1 = "data/filtrations/$$$.txt" # IMPORT PATHS!
    path2 = "data/filtrations/$$$.txt"
    filtration1 = np.loadtxt(path1)
    filtration2 = np.loadtxt(path2)

    comparison = Comparer(filtration1, filtration2)
    distance = comparison.calculateKDEdistance()
    print(distance)