import pdb
class TreeNode(object):
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None
		self.next=None
        
    
	def insertn(self,data):
		self.new_dat=data
		if self.data>self.new_dat:
			if self.right==None:
				self.right=TreeNode(self.new_dat)
			else:
				self.right.insertn(self.new_dat)
		else:
			if self.left==None:
				self.left=TreeNode(self.new_dat)
			else:
				self.left.insertn(self.new_dat)
				
		
	def inordr(self):
		pdb.set_trace()
		if self:
			self.next=self
			if self.left!=None:
				self.left.inordr()
			if self.right!=None:
				self.right.inordr()
				
			
class Solution(object):
	def __init__(self):
		self.root=None

	def insrt(self,data):
		self.newdata=data
		if self.root==None:
			self.root=TreeNode(self.newdata)
		else:
			self.root.insertn(self.newdata)

	def flatten(self):
		"""
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		self.root.inordr()
        
        
sol=Solution()
sol.insrt(20)
sol.insrt(10)
sol.insrt(30)
sol.insrt(5)
sol.insrt(15)
sol.flatten()