# @Author: Hsien-Che Charles Chen
# @Date:   02-17-2017
# @Project: HW3
# @Last modified by:   Hsien-Che Charles Chen
# @Last modified time: 02-17-2017

from attributes import *
from decision_tree_util import *


# Thank you Stack Overflow for basic template binary tree.
class Node:
	def __init__(self, df, threshhold, entropy):
		self.l = None
		self.r = None
		self.t = threshhold
		self.df = df
		self.e = entropy

class DTree:
	def __init__(self, df):
		self.root = Node(df, 0.0, -1.0)

	def getRoot(self):
		return self.root

	# Run ID3 algorithm at unresolved node.
	def ID3(self):
		if self.root.e <= 0:
			self._resolve(self.root)
		else:
			print "DTree has already been resolved."

	def _resolve(self, node):
		# Calculate current node entropy.
		node.e = entropyFromDF(node.df)

		# Base case
		if node.e == 0:
			return

		# Create Attributes
		attr = calcAttribute(node.df["vect"].copy())

		# Select best attributes
		best = bestAttrWithEntropy(node.df, attr, node.e)
		thresh = best[0]
		dim = best[1]

		# Create Children Nodes with new parameters
		df = node.df
		# Yes
		node.l = Node(df[df.apply(lambda x: x['vect'][dim] <= thresh, axis = 1)], 0.0, -1.0)
		node.r = Node(df[df.apply(lambda x: x['vect'][dim] > thresh, axis = 1)], 0.0, -1.0)

		# Resolve Those Nodes.
		_resolve(node.l)
		_resolve(node.r)

		# Remove dataframe reference in this node to save memory
		node.v = None

	def restart(self):
		self.root = None

	def printTree(self):
		if(self.root != None):
			self._printTree(self.root)

	def _printTree(self, node):
		if(node != None):
			self._printTree(node.l)
			print str(node.v) + ' '
			self._printTree(node.r)
