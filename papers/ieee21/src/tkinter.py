import pickle
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import dionysus as d


img = cv.imread("../data/test.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.namedWindow("Butt Cancer")




pointcloud = []

rows, cols = gray.shape
for y in range(rows):
	for x in range(cols):
		if(gray[y,x] < 150):
			pointcloud.append([x,y])
			gray[y,x] = 0
		else:
			gray[y,x] = 255



cv.imshow("Butt Cancer", gray)
cv.waitKey(0)
cv.destroyAllWindows()



'''
#Cool, now we have our pointcloud, lets plot it to make sure it looks right
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

for (xp, yp) in pointcloud:
	ax.scatter(xp,yp)

plt.title('Pointcloud')
plt.show()

plt.scatter(pointcloud[:,0], pointcloud[:,1])
'''

#Run thru

#print(pointcloud)
ripspoints = (np.array(pointcloud))
#print(ripspoints)
f = d.fill_rips(pointcloud, 2, )


#Output with open('output.txt', 'w')
#dionysus (import dionysus as d)
for x in f:
	print("Simplex :", x)
