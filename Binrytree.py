class Node(object):
	def __init__(self, data):
		"""
		Node Constructor
		@param data node data object
		"""
		self.left = None
		self.right = None
		self.data = data

	def __repr__(self):
		return "Node With Data: %d" % self.data

	def insert(self, data):
		"""
		Insert new node with data
		@param data node data object to insert
		"""
		if data < self.data:
			if self.left is None:
				self.left = Node(data)
			else:
				self.left.insert(data)
		else:
			if self.right is None:
				self.right = Node(data)
			else:
				self.right.insert(data)

	def lookup(self, data, parent=None):
		"""
		Lookup node containing data
		@param data node data object to look up
		@param parent node's parent
		@returns node and node's parent if found or None, None
		"""
		if data < self.data:
			if self.left is None:
				return None, None
			return self.left.lookup(data, self)
		elif data > self.data:
			if self.right is None:
				return None, None
			return self.right.lookup(data, self)
		else:
			return self, parent

	def children_count(self):
		"""
		Returns the number of children for a given node
		@returns number of children: 0, 1, 2
		"""
		count = 0
		if self.left:
			count += 1
		if self.right:
			count += 1
		return count

	def descendant_count(self):
		"""
		Counts all descendant nodes
		"""
		count = 0
		if self.left:
			count += 1 + self.left.descendant_count()
		if self.right:
			count += 1 + self.right.descendant_count()
		return count

	def delete(self, data):
		"""
		Delete node containing data
		@param data node's content to delete
		"""
		node, parent = self.lookup(data)
		if node:
			children_count = node.children_count()
			if children_count == 0:
				# If node has no children then remove it
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
				del node
			elif children_count == 1:
				if node.left:
					child = node.left
				else:
					child = node.right
				if parent:
					if parent.left is node:
						parent.left = child
					else:
						parent.right = child
				del node
			else:
				parent = node
				successor = node.right
				while successor.left:
					parent = successor
					successor = successor.left
				node.data = successor.data
				if parent.left == successor:
					parent.left = successor.right
				else:
					parent.right = successor.right
	def inorder_print(self):
		if self.left:
			self.left.print_tree()
		print self.data
		if self.right:
			self.right.print_tree()

	def print_each_level(self):
		# Start off with root node
		thislevel = [self]

		# While there is another level
		while thislevel:
			nextlevel = list()
			#Print all the nodes in the current level, and store the next level in a list
			for node in thislevel:
				print node.data
				if node.left: nextlevel.append(node.left)
				if node.right: nextlevel.append(node.right)
			print
			thislevel = nextlevel



root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
print root.lookup(10)
root.insert(13)
root.delete(10)
print root.lookup(10)