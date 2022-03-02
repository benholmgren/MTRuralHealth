import math

import Img
import Persist
import math as m
import sys
import numpy as np

def generateFiltrationMatrix(inputFile, outputFile, outputPath):
	cloud = Img.cloud(inputFile, 80, 4)

	diag = Persist.run_rips(cloud)

	arr_diag = []
	for point in diag[0]:
		if point.death != math.inf:
			arr_diag.append([point.birth, point.death])

	return np.array(arr_diag)





def export(filtrationMatrix, outputFile, outputPath):
	file = open(sys.path[0]+outputPath+'/'+outputFile, 'w+')
	for line in filtrationMatrix:
		file.write(str(line[0]) + " " + str(line[1]) + "\n")
	file.close()

if __name__ == '__main__':
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	outputPath = sys.argv[3]
	filtrationMatrix = generateFiltrationMatrix(inputFile, outputFile, outputPath)
	export(filtrationMatrix, outputFile, outputPath)

