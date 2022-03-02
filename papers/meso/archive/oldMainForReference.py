import math

import data.Img
import data.Persist
import math as m


if __name__ == '__main__':
    print("cloud1")
    cloud_ok_1 = Img.cloud("data/stad1.1.png", 80, 4)
    print("cloud2")
    cloud_ok_2 = Img.cloud("data/stad1.2.png", 80, 4)
    diag_1 = Persist.run_rips(cloud_ok_1)
    diag_2 = Persist.run_rips(cloud_ok_2)

    arr_diag1 = []
    arr_diag2 = []

    for point in diag_1[0]:
        if point.death != math.inf:
            arr_diag1.append([point.birth, point.death])
    print(arr_diag1)

    for point in diag_2[0]:
        if point.death != math.inf:
            arr_diag2.append([point.birth, point.death])

    Persist.kde_dist(arr_diag1, arr_diag2)



