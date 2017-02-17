# @Author: Hsien-Che Charles Chen
# @Date:   02-17-2017
# @Project: PA4
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-17-2017
import pandas as pd
import numpy as np
import math as mt
import time

# Custom Files #
import data_loader as ld
import decision_tree as dt

def printErrors(tree):
	trainingData = ld.readFile("hw3train.txt")

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
