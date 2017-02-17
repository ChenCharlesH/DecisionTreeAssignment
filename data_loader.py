# @Author: Hsien-Che Charles Chen
# @Date:   02-03-2017
# @Project: HW3
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-13-2017
# @Desc.: Requires Python 2.7 + Anaconda.

import pandas as pd
import numpy as np
import csv

# Indentifier is for embedding index info into the Pandas array.
COLUMNS = ['vect', 'label', 'identifier']
LABEL_OFFSET = -2

# Read the file into DataFrame.
def readFile(fileName):
	with open(fileName) as file:
		reader = csv.reader(file, delimiter= ' ')
		lis = {COLUMNS[0]: [], COLUMNS[1]: [], COLUMNS[2] : []}
		count = 0
		for row in reader:
			values = []
			for x in row[:LABEL_OFFSET]:
				values.append(float(x))
			lis[COLUMNS[0]].append(np.array(values))
			lis[COLUMNS[1]].append(float(row[LABEL_OFFSET]))
			lis[COLUMNS[2]].append(count)
			count = count + 1


		data = pd.DataFrame(lis, columns = COLUMNS)
		return data
