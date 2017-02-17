# @Author: Hsien-Che Charles Chen
# @Date:   02-03-2017
# @Project: HW3
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-16-2017
# @Desc.: Requires Python 2.7 + Anaconda.

import pandas as pd
import numpy as np
import math as mt
import time

# Custom Files #
import data_loader as ld
from decision_tree_util import *
from attributes import *


def main():
	trainingData = ld.readFile("hw3train.txt")
	attr = calcAttribute(trainingData["vect"])
	print attr

if __name__ == "__main__":
	t0 = time.time()
	main()
	t1 = time.time()
	print "\n\nTotal Run Time: " + str(t1-t0) + "secs"
