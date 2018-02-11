class Node(object):
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
class BinaryTree(object):
	def __init__(self):
		self.root=None
		
	def get_sum(self,nde):
		if nde is None:
			return 0
		else:
			#sum=nde.data
			sum=nde.data+self.get_sum(nde.left)+self.get_sum(nde.right)
		return sum
bt=BinaryTree()
bt.root=Node(1)
bt.root.left=Node(45)
bt.root.right=Node(10)
bt.root.left.right=Node(10)
ans=bt.get_sum(bt.root)
print(ans)