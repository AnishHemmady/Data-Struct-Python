'''
Lets see Binary Tree
Program by Anish Hemmady
Complete binary tree with insertion and deletion
avl tree.
Traversal complete
Quite good program
'''
import pdb
import copy
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		self.height=None
		
	def grab_lft(self):
		return self.left
		
	def set_lft(self,lfty):
		self.left=lfty
		
	def grab_rght(self):
		return self.right
		
	def set_rght(self,rght):
		self.right=rght
		
		
	def find_height(self,curr):
		#pdb.set_trace()
		if curr==None:
			return 0
		else:
			value=(1+max(self.find_height(curr.left),self.find_height(curr.right)))
			
		return value
		
	def inorder_trav(self):
		#pdb.set_trace()
		
		if self:
			if self.left!=None:
				self.left.inorder_trav()
			print self.data
			
			if self.right!=None:
				self.right.inorder_trav()
				
	def preorder_trav(self):
		#pdb.set_trace()
		print self.data
		if self:
			if self.left!=None:
				self.left.preorder_trav()
			
			if self.right!=None:
				self.right.preorder_trav()
				
				
	def postorder_trav(self):
		#pdb.set_trace()
	
		if self:
			if self.left!=None:
				self.left.postorder_trav()
			
			if self.right!=None:
				self.right.postorder_trav()
				
			print self.data
			
	def imblcne_fctr(self,curr):
		#pdb.set_trace()
		if curr==None:
			return 0
		else:
			value=(self.find_height(curr.left)-self.find_height(curr.right))
		
		return value
	def lft_rote(self,curr):
		x1=curr.right
		t2=x1.left
		x1.left=curr
		curr.right=t2
		curr.height=self.find_height(curr)
		x1.height=self.find_height(x1)
		return x1
		
	def rght_rote(self,curr):
		#pdb.set_trace()
		x1=curr.left
		t2=x1.right
		x1.right=curr
		curr.left=t2
		curr.height=self.find_height(curr)
		x1.height=self.find_height(x1)
		return x1
		
	def insrt(self,data):
		#pdb.set_trace()
		self.new_dat=data
		if self.new_dat>self.data:
			if self.right==None:
				self.right=Node(self.new_dat)	
			else:
				self.right=self.right.insrt(self.new_dat)
				
		else:
			if self.left==None:
				self.left=Node(self.new_dat)
			else:
				self.left=self.left.insrt(self.new_dat)
				
		self.height=self.find_height(self)
		#pdb.set_trace()
		imblnce=self.imblcne_fctr(self)
		if imblnce>1 and self.new_dat<self.left.data:
			self=self.rght_rote(self)
			
		elif imblnce<-1 and self.new_dat>self.right.data:
			self=self.lft_rote(self)
			
		elif imblnce>1 and self.new_dat>self.left.data:
			self.left=self.lft_rote(self.left)
			self=self.rght_rote(self)
		elif imblnce<-1 and self.new_dat<self.right.data:
			self.right=self.rght_rote(self.right)
			self=self.lft_rote(self)
		return self
		
		
		
		
	
class Bnry_tree:
	def __init__(self):
		self.root=None
		
	def insrt_nde(self,data):
		#pdb.set_trace()
		self.dat=data
		new_nde=Node(self.dat)
		if self.root==None:
			self.root=new_nde
		else:
			self.rooty=self.root
			while self.rooty!=None:
				if self.dat<self.rooty.data:
					temp=self.rooty
					self.rooty=self.rooty.left
				else:
					temp=self.rooty
					self.rooty=self.rooty.right
					
			self.rooty=new_nde
			if self.rooty.data<temp.data:
				temp.left=self.rooty
			else:
				temp.right=self.rooty
					
	def	innsrt(self,dat):
		self.dat=dat
		if self.root==None:
			self.root=Node(self.dat)
		else:
			self.root.insrt(self.dat)
			
				
	def insrt_recur(self,dat):
		#pdb.set_trace()
		self.dat=dat
		if self.root==None:
			new_nde=Node(self.dat)
			self.root=new_nde
		else:
			self.insertnn(self.dat,self.root,temp=None)
			
	def insertnn(self,new_dat,root,temp):
			#pdb.set_trace()
			self.new_dat=new_dat
			self.rooty=root
			self.temp=temp
			if self.rooty==None:
				new_node=Node(self.dat)
				self.rooty=new_node
				if self.rooty.data<self.temp.data:
					self.temp.left=self.rooty
				else:
					self.temp.right=self.rooty
					
			elif self.rooty.data>self.new_dat:
				self.temp=self.rooty
				self.rooty=self.rooty.left
				if self.rooty!=None:
					self.new_dat=self.rooty.data
				self.insertnn(self.new_dat,self.rooty,self.temp)
			else:
				self.temp=self.rooty
				self.rooty=self.rooty.right
				if self.rooty!=None:
					self.new_dat=self.rooty.data
				self.insertnn(self.new_dat,self.rooty,self.temp)
	
	
	def convrt_lnkdlst(self):
		curr=self.root
		self.convrsn_lkd(curr)
	
	def convrsn_lkd(self,curr):
		pdb.set_trace()
		if curr==None:
			return curr
		temp=curr.right
		if curr.left!=None:
			curr.right=curr.left
			curr.left=None
			curr=self.convrsn_lkd(curr.right)
			
		if temp!=None:
			curr.right=temp
			curr=self.convrsn_lkd(curr.right)
		return curr
		
	def summng_vals(self):
		curr=self.root
		self.sumz_vals(curr)
		
	def sumz_vals(self,curr):
		pdb.set_trace()
		if curr==None:
			return 0
		old_val=curr.data
		curr.data=self.sumz_vals(curr.left)+self.sumz_vals(curr.right)
		return curr.data+old_val
	
	def mirror_it(self):
		curr=self.root
		self.mirror(curr)
	
	def mirror(self,curr):
		#pdb.set_trace()
		if curr==None:
			return
		else:
			self.mirror(curr.left)
			self.mirror(curr.right)
			temp=curr.right
			curr.right=curr.left
			curr.left=temp
			
			
	def fnd_min(self):
		if self.root==None:
			return "root is null"
		else:
			curr=self.root
			while(curr.left!=None):
				curr=curr.left
			return curr.data
			
	def fnd_minm_sub(self,root):
		curr=root
		while(curr.left!=None):
			curr=curr.left
		return curr
			
	def set1_height(self,curr):
		#pdb.set_trace()
		if curr==None:
			return 0
		else:
			value=(1+max(self.set1_height(curr.left),self.set1_height(curr.right)))
			curr.height=value
		return value
		
			
	def fnd_max(self):
		if self.root==None:
			return "root is null"
		else:
			curr=self.root
			while(curr.right!=None):
				curr=curr.right
			return curr.data
			
	def fnd(self,dat):
		#pdb.set_trace()
		self.curr=self.root
		if self.curr==None:
			return "cant be found"
		else:
			found=False
			while self.curr!=None and found==False:
				if self.curr.left!=None:
					if self.curr.left.data==dat:
						found=True
						self.actul_loc=self.curr.left
				if self.curr.right!=None:
					if self.curr.right.data==dat:
						found=True
						self.actul_loc=self.curr.right
				if found==False and self.curr!=None:
					if self.curr.data<dat:
						self.curr=self.curr.right
					else:
						self.curr=self.curr.left
					
					
		if found==True:
			return self.curr,self.actul_loc
		else:
			return"element not found"
			
	def set_height_nde(self):
		
		if self.root.height==None:
			#pdb.set_trace()
			value=self.find_height(self.root)
			
		
	def fnd_lca(self,dat1,dat2):
		rooty=self.root
		data1=dat1
		data2=dat2
		vals=self.findlca(data1,data2,rooty)
		return vals.data

	def findlca(self,new1,new2,curr):
		#pdb.set_trace()
		if curr==None:
			return None
		elif(new1>curr.data and new2>curr.data):
			return self.findlca(new1,new2,curr.right)
		elif(new1<curr.data and new2<curr.data):
			return self.findlca(new1,new2,curr.left)
		else:
			return curr
		
	def chck_blnce_fctr(self):
		curr=self.root
		blnce=curr.left.height-curr.right.height
		if blnce>1:
			if curr.left.height>curr.right.height:
				self.find_imblnce_nde(curr.left)
			else:
				curr_nde,nxt_info=self.find_imblnce_nde(curr.right)
				self.correct_blnce(curr_nde,nxt_info)
		else:
			return "its balnced"
			
	def find_imblnce_nde(self,curr):
		pdb.set_trace()
		if curr!=None:
			rght_heavy=False
			left_heavy=False
			if curr.left==None and curr.right!=None:
				blnce_fctr=-1-curr.right.height
				rght_heavy=True
			elif curr.right==None and curr.left!=None:
				blnce_fctr=curr.left.height-(-1)
				left_heavy=True
			else:
				blnce_fctr=curr.left.height-curr.right.height
				if curr.left.height>curr.right.height:
					left_heavy=True
				else:
					rght_heavy=True
				
		if blnce_fctr>1 or blnce_fctr<-1:
			rght_lft=[-1]*2
			ret_curr=curr
			if rght_heavy==True:
				rght_lft[1]=0
			else:
				rght_lft[0]=0
			return ret_curr,rght_lft
			
		else:
			if rght_heavy==True:
				currnt,lst=self.adjst_blnce(curr.right)
			else:
				currnt,lst=self.adjst_blnce(curr.left)
				
		return currnt,lst
	
	
	
			
				
	def findng_data(self,data):
		self.dat=data
		previous,value=self.fndng_urslf(self.dat,self.root,prev=self.root)
		if value=="Found Nothing":
			return value
		else:
			return previous,value
		
	def fndng_urslf(self,daty,curr,prev):
		if curr==None:
			return prev,"Found Nothing"
		elif daty<curr.data:
			prev=curr
			return self.fndng_urslf(daty,curr.left,prev)
		elif daty>curr.data:
			prev=curr
			return self.fndng_urslf(daty,curr.right,prev)
		else:
			return prev,curr
			
			
		
	
	
		
	def delte(self,dat):
		self.data1=dat
		parent,node=self.findng_data(self.data1)
		'''
		deletion of child node
		'''
		if node.left==None and node.right==None and parent==self.root:
				#pdb.set_trace()
			if parent.right==node:
				temp=parent.left.right
				temp1=parent.left
				parent.left=temp
				parent.right=None
				self.root=temp1
				self.root.right=parent
			elif parent.left==node:
				#pdb.set_trace()
				temp=parent.right.left
				temp1=parent.right
				parent.right=temp
				parent.left=None
				self.root=temp1
				self.root.left=parent
			self.set1_height(self.root)
			
					
				
		elif node.left==None and node.right==None:
			if parent.left!=None:
				if parent.left.data==node.data:
					parent.left=None
			if parent.right!=None:
				if parent.right.data==node.data:
					parent.right=None
			self.set1_height(self.root)
			
		elif node.left==None or node.right==None:
			if parent.left!=None:
				if parent.left.data==node.data:
					if node.left==None:
						parent.left=node.right
					else:
						parent.left=node.left
			if parent.right!=None:
					if parent.right.data==node.data:
						if node.left==None:
							parent.right=node.right
						else:
							parent.right=node.left
			self.set1_height(self.root)
		else:
			minm=self.fnd_minm_sub(node.right)
			parent2=node.right
			node.data=minm.data
			if parent2.right==None and parent2.left==None:
				if node.left!=None:
					if node.left.data==minm.data:
						node.left=None
				if node.right!=None:
					if node.right.data==minm.data:
						node.right=None
				self.set1_height(self.root)
						
			elif parent2.right==None or parent2.left==None:
				if parent2.right!=None:
					node.right=parent2.right
				else:
					node.right=None
				
					
				self.set1_height(self.root)
			
			else:
				return "cant delete"
			
						
	def inordr(self):
		self.root.inorder_trav()
		
	def preordr(self):
		self.root.preorder_trav()
		
	def postordr(self):
		self.root.postorder_trav()
	
	
		
	
br=Bnry_tree()
br.innsrt(23)
br.innsrt(10)
br.innsrt(25)
br.innsrt(24)
br.innsrt(26)
br.innsrt(11)
br.innsrt(7)
br.innsrt(12)
br.innsrt(5)
br.innsrt(3)
print br.root.height
print br.fnd_lca(26,5)
#br.convrt_lnkdlst()
br.summng_vals()
#br.delte(12)
'''br.delte(3)
br.delte(5)
br.delte(11)
br.delte(7)
br.delte(12)
br.delte(10)
br.mirror_it()'''
#print br.findng_data(27)
#print br.preordr()
#print br.root.height
#br.imblcne_fctr()
#print br.set_height_nde()
#br.blnce_fctr()
'''br.delte(25)
print br.fnd(25)
print br.inordr()
print br.preordr()
print br.postordr()'''



				
				
			
			
		