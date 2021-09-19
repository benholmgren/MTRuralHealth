import pickle
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread("../data/test.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.namedWindow("Butt Cancer")





cv.imshow("Butt Cancer", gray)
cv.waitKey(0)
cv.destroyAllWindows()

pointcloud = []

rows, cols = gray.shape
for y in range(rows):
	for x in range(cols):
		if(gray[y,x] < 200):
			pointcloud.append((x,y))



#Cool, now we have our pointcloud, lets plot it to make sure it looks right
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for (xp, yp) in pointcloud:
	ax.scatter(xp,yp)

plt.title('Pointcloud')
plt.show()

plt.scatter(pointcloud[:,0], pointcloud[:,1])
