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

print(gray.shape)
for y in range(rows):
	for x in range(cols):
		if(gray[y,x] < 150):
			pointcloud.append([x,rows - y])
			gray[y,x] = 0
		else:
			gray[y,x] = 255



cv.imshow("Butt Cancer", gray)
cv.waitKey(0)
cv.destroyAllWindows()



#Cool, now we have our pointcloud, lets plot it to make sure it looks right
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

#Run thru

#print(pointcloud)
ripspoints = (np.array(pointcloud).astype('f4'))
print(ripspoints)

testpoints = []

testpoints.append([1,2])
testpoints.append([2,3])
testpoints.append([0,0])
testarray = np.array(testpoints).astype('f4')


print('number of pixels: ',  len(pointcloud))
'''
for (xp, yp) in pointcloud:
	ax.scatter(xp,yp)
'''
print(pointcloud[0][:])
ax.scatter(ripspoints[:,0], ripspoints[:,1])

plt.title('Pointcloud')
plt.show()



print('Generating filtration for img01')
f = d.fill_rips(ripspoints, 2, 2)
f.sort()


#Output with open('output.txt', 'w')
#dionysus (import dionysus as d)
output = open('output.txt', 'w+')

print('writing rips filtration data to output file')
for simplex in f:
	
	output.write(str(simplex.data))
	

m = d.homology_persistence(f)
dgms = d.init_diagrams(m,f)
print('Plotting diagram for H1')
d.plot.plot_diagram(dgms[1], show= True)

print('writing pd data to diagrams.txt')
diagrams = open('diagrams.txt', 'w+')
for l, dgm in enumerate(dgms):
	#print('hi')
	for pt in dgm:
		diagrams.write("H")
		diagrams.write(str(l))
		diagrams.write("_Birth_")
		diagrams.write(str(pt.birth))
		diagrams.write("_Death_")
		diagrams.write(str(pt.death))
		diagrams.write('\n')
output.close()
diagrams.close()
print('DONE')
