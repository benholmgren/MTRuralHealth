import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# In: filename (string), threshold pixel value (int in [0, 255]),
# discretization parameter (natural)
# Out: greyscale image (if desired) and point cloud np array
def cloud(filename, threshold, disc):
    img = cv.imread(filename)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.namedWindow("sample")

    pointcloud = []

    rows, cols = gray.shape

    for y in range(rows):
        for x in range(cols):
            if(gray[y,x] < threshold):
                if x % disc == 0 or y % disc == 0:
                    pointcloud.append([x,rows - y])
                gray[y,x] = 0
            else:
                gray[y,x] = 255


    # FOR VISUALIZATION, UNCOMMENT:
    # For grayscale image:
    #cv.imshow("sample", gray)
    #cv.waitKey(0)
    #cv.destroyAllWindows()

    # For plot of point cloud:
    x = [x[0] for x in pointcloud]
    y = [y[1] for y in pointcloud]

    plt.scatter(x, y, s=0.05)
    plt.show()

    out_cloud = (np.array(pointcloud).astype('f4'))
    return out_cloud


