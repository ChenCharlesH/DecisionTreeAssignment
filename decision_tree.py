# @Author: Hsien-Che Charles Chen
# @Date:   02-17-2017
# @Project: HW3
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-17-2017

from attributes import *
from decision_tree_util import *

MAX_HEIGHT = 100000

# Thank you Stack Overflow for basic template binary tree.
class Node:
	def __init__(self, df, threshhold, entropy, feature):
		self.l = None
		self.r = None
		self.t = threshhold
		self.df = df
		self.ft = feature
		self.e = entropy

	def display(self):
		return "( " + "x_" + str(self.ft) + ": <=  " + str(self.t) + " )"


class DTree:
	def __init__(self, df):
		self.root = Node(df, 0.0, -1.0, -1)
		self.height = 0

	def getRoot(self):
		return self.root

	# Classify the Vector
	def classifyVect(self, vector):
		return self._classifyVect(self.root, vector)

	def _classifyVect(self, node, vector):
		# Base
		if node.e == 0:
			return node.df["label"].iloc[0]
		elif vector[node.ft] <= node.t:
			return self._classifyVect(node.l, vector)
		else:
			return self._classifyVect(node.r, vector)


	# Run ID3 algorithm at unresolved node.
	def ID3(self):
		if self.root.e <= 0:
			self._resolve(self.root, 0)
		else:
			print "DTree has already been resolved."

	def _resolve(self, node, level):
		# Calculate current node entropy.
		node.e = entropyFromDF(node.df)

		# Base case
		if node.e == 0 or level == MAX_HEIGHT:
			return

		# Create Attributes
		attr = calcAttribute(node.df["vect"].copy())

		# Select best attributes
		best = bestAttrWithEntropy(node.df, attr, node.e)
		thresh = best[0]
		dim = best[1]

		# Create Children Nodes with new parameters
		df = node.df
		node.ft = dim
		node.t = thresh
		# Yes
		node.l = Node(df[df.apply(lambda x: x['vect'][dim] <= thresh, axis = 1)], -1, -1.0, 0)
		node.r = Node(df[df.apply(lambda x: x['vect'][dim] > thresh, axis = 1)], -1, -1.0, 0)

		# Remove dataframe reference in this node to save memory
		node.v = None

		# Resolve Those Nodes.
		print "Going to left node."
		self._resolve(node.l, level + 1)
		print "Going to right node."
		self._resolve(node.r, level + 1)
		if level + 1 > self.height:
			print "HEIGHT: " + str(level + 1)
			self.height = level + 1

	def restart(self):
		self.root = None
		self.height = 0

	def printLevelOrder(self):
		counter = 1
		while counter <= self.height:
			print "Level " + str(counter) + " :"
			self.printTreeLevel(counter)
			counter += 1

	# Print by Level
	def printTreeLevel(self, level):
		if(self.root != None):
			self._printTreeLevel(self.root, level)

	def _printTreeLevel(self, node, level):
		if node == None:
			return
		if level == 1:
			print node.display()
		else:
			self._printTreeLevel(node.l, level - 1)
			self._printTreeLevel(node.r, level - 1)
