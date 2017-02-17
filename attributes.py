import math as mt
import pandas as pd
import numpy as np

from operator import itemgetter


# Get attrbutes of a specific vector
# gets the mid point between two vectors
# Should be input by a data frame of vectors.
# Returns Data frame with 1 by m-1.
# Input will be sorted.
def calcSingleAttribute(select, vectors):
	if select < 0 or vectors[0].size < select:
		return pd.DataFrame();

	vectSize = vectors.size

	arr = vectors.as_matrix()
	# Sort array by axis

	# Convert to list.
	for index, vect in np.ndenumerate(arr):
		vectors[index] = vect.tolist()

	arr = arr.tolist()
	arr = sorted(arr, key = itemgetter(select))

	ls = []
	indLs = []

	# Take the x element of the vectors and calculate the midpoint
	# between each element.
	# Should have one element less than the original size.
	for index, vect in enumerate(arr):
		if index == vectSize - 1:
			break

		indLs.append(index)
		ls.append((vect[select] + arr[index + 1][select])/2.0)

	return pd.Series(ls, index = indLs)


# Calculate attributes of each column within the vector.
# Uses multi-threading.
def calcAttribute(vectors):
	lim = vectors[0].size
	count = 0
	results = []

	# Call everything
	while count < lim:
		# results.append(calcSingleAttribute(count, vectors.copy()))
		results.append(calcSingleAttribute(count, vectors.copy()))
		count += 1

	# Merge
	result = pd.concat(results, axis = 1)
	return result
