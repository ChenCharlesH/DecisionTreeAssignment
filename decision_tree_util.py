# @Author: Hsien-Che Charles Chen
# @Date:   02-03-2017
# @Project: HW3
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-16-2017
# @Desc.: Requires Python 2.7 + Anaconda.

import math as mt
import pandas as pd
import numpy as np

def smallestAttributeWithEntropy():
	return 

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
