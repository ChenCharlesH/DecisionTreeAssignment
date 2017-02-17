# @Author: Hsien-Che Charles Chen
# @Date:   02-17-2017
# @Project: HW3
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-17-2017
import pandas as pd
import numpy as np
import math as mt
import time
import copy

# Custom Files for Loading and Printing Stuff #
import data_loader as ld
import decision_tree as dt

def prune(tree):
	countRemoved = 0
	validData = ld.readFile("hw3validation.txt")


	# Call it twice
	tree1 = copy.deepcopy(tree)
	return BFSPrune(tree, tree1, validData)

def BFSPrune(notouchtree, compTree, data):
	counter = 1
	while counter <= notouchtree.height:
		if BFSPruneLevel(notouchtree, compTree, compTree.root, counter, data) == True:
			print "Removed Node"
			break
		counter += 1
	return compTree

def BFSPruneLevel(tree, compTree, node, level, data):
	result = False
	if node == None:
		return False
	if level == 1:
		result = actualPrune(tree, compTree, node, data)
		if result == True:
			return True
	else:
		BFSPruneLevel(tree, compTree, node.l, level - 1, data[data.apply(lambda x: x['vect'][node.ft] <= node.t, axis = 1)])
		result = actualPrune(tree, compTree, node, data)
		if result == True:
			return True
		BFSPruneLevel(tree, compTree, node.r, level - 1, data[data.apply(lambda x: x['vect'][node.ft] > node.t, axis = 1)])

	return result

def actualPrune(tree, compTree, node, data):
	tempLeft = node.l
	node.l = None
	tempRight = node.r
	node.r = None
	tempE = node.e
	node.e = 0
	tempDF = node.df

	majority = data["label"].mode()
	if majority.size <= 0:
		return False
	majority = majority[0]

	# Get Majority
	node.df = data[data.apply(lambda x: x['label'] == majority, axis = 1)]

	if errors(compTree, data) <= errors(tree, data):
		return True

	node.l = tempLeft
	node.r = tempRight
	node.df = tempDF
	node.e = tempE

	return False

def errors(tree, data):
	wrong = 0
	size = data["vect"].size
	for index, vect in data["vect"].iteritems():
		if data["label"][index] != tree.classifyVect(vect):
			wrong += 1
	return float(wrong) / size

def printErrors(tree):
	trainingData = ld.readFile("hw3train.txt")

	wrong = 0
	size = trainingData["vect"].size

	# Calculate training error.
	for index, vect in trainingData["vect"].iteritems():
		if trainingData["label"][index] != tree.classifyVect(vect):
			wrong += 1

	print "Training error: " + str((float(wrong) / size))

	validData = ld.readFile("hw3validation.txt")
	wrong = 0
	size = validData["vect"].size
	for index, vect in validData["vect"].iteritems():
		if validData["label"][index] != tree.classifyVect(vect):
			wrong +=1

	print "Validation error: " + str((float(wrong) / size))

	# Calculate test error
	testData = ld.readFile("hw3test.txt")
	wrong = 0
	size = testData["vect"].size
	for index, vect in testData["vect"].iteritems():
		if testData["label"][index] != tree.classifyVect(vect):
			wrong += 1

	print "Test Error: " + str(float(wrong) / size)
