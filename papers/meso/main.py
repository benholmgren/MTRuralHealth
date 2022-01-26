import Img
import Persist
import math as m


if __name__ == '__main__':
    print("cloud1")
    cloud_ok_1 = Img.cloud("data/stad1.1.png", 80, 4)
    print("cloud2")
    cloud_ok_2 = Img.cloud("data/stad1.2.png", 80, 4)
    diag_1 = Persist.run_rips(cloud_ok_1)
    diag_2 = Persist.run_rips(cloud_ok_2)
    print(Persist.wass_dist(diag_1[0], diag_2[0]))


