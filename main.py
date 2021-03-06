# @Author: Hsien-Che Charles Chen
# @Date:   02-03-2017
# @Project: HW3
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-17-2017
# @Desc.: Requires Python 2.7 + Anaconda.

import pandas as pd
import numpy as np
import math as mt
import time

# Custom Files #
import data_loader as ld
import decision_tree as dt

def main():
	trainingData = ld.readFile("hw3train.txt")
	tree = dt.DTree(trainingData)
	tree.ID3()

	wrong = 0
	size = trainingData["vect"].size

	# Calculate training error.
	for index, vect in trainingData["vect"].iteritems():
		if trainingData["label"][index] != tree.classifyVect(vect):
			wrong += 1

	print "Training error: " + str((float(wrong) / size))

	# Calculate test error
	testData = ld.readFile("hw3test.txt")
	wrong = 0
	size = testData["vect"].size
	for index, vect in testData["vect"].iteritems():
		if testData["label"][index] != tree.classifyVect(vect):
			wrong += 1

	print "Test Error: " + str(float(wrong) / size)

	return tree


if __name__ == "__main__":
	t0 = time.time()
	main()
	t1 = time.time()
	print "\n\nTotal Run Time: " + str(t1-t0) + "secs"
