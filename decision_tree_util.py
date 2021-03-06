# @Author: Hsien-Che Charles Chen
# @Date:   02-03-2017
# @Project: HW3
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-17-2017
# @Desc.: Requires Python 2.7 + Anaconda.

import math as mt
import pandas as pd
import numpy as np


# Returns the best attribute using entropy.
# Attributes should be formatted as defined and returned in attributes.py
def bestAttrWithEntropy(df, attr, baseEntropy):
	infoGain = -1
	threshold = -1

	indexResult = -1
	for index, sAttr in enumerate(attr):
		# Drop duplicates in attributes.
		sAttr = sAttr.drop_duplicates()
		# Iterate through each value.
		for attrIndex, thresh in sAttr.iteritems():
			copyDf = df.copy()
			# Convert Vectors to a Single Attribute for Easy Compare
			copyDf['vect'] = copyDf['vect'].apply(lambda x: x[index])
			df1 = copyDf[copyDf['vect'] <= thresh]
			df2 = copyDf[copyDf['vect'] > thresh]
			en1 = entropyFromDF(df1)
			en2 = entropyFromDF(df2)

			totSize = df1.size + df2.size
			prob1 = df1.size / totSize
			prob2 = df2.size / totSize

			# Split into two branches.
			total = prob1 * en1 + prob2 * en2
			locInfoGain = baseEntropy - total
			if locInfoGain > infoGain:
				infoGain = locInfoGain
				threshold = thresh
				indexResult = index

	return (threshold, indexResult)

# Calculate H(x) Entropy Based off DF from loader.
def entropyFromDF(df):
	if df.empty:
		return 0.0

	labels = df["label"]
	labels = labels.value_counts()
	total = labels.sum()
	prob = []

	for i, value in labels.iteritems():
		prob.append(float(value) / total)

	return entropy(prob)

# Takes a list of numbers.
def entropy(listProb):
	# Make sure everything adds up to less than 1.
	counter = 0
	for x in listProb:
		counter += x

	if counter > 1:
		print "**ERROR** Non-Prob List for: " + str(listProb)
		print "TERMINATING PROGRAM"
		exit()

	result = 0
	for x in listProb:
		# Check if zero
		if x == 0:
			result += 0
		else:
			result += -x * mt.log(x)

	if result < 0:
		print "Warning: Entropy is negative for: " + str(listProb)

	return result
