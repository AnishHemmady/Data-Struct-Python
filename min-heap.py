'''
mini-max heap
'''
import sys
import pdb
class Min_heap:
	
	def __init__(self,maxsze):
		self.maxsze=maxsze
		self.size=0
		self.heap=[None]*(self.maxsze+1)
		minm=-sys.maxint-1
		self.heap[0]=minm
		self.front=1
		
	def parent(self,pos):
		return pos/2
		
	def leftchld(self,pos):
		return(2*pos)
		
	def rghtchld(self,pos):
		return(2*pos+1)
		
	def isleaf(self,pos):
		if pos>=self.maxsze/2 and pos<=self.size:
			return True
		return False
		
	def swapy(self,frst,secnd):
		self.heap[frst],self.heap[secnd]=self.heap[secnd],self.heap[frst]
		
	def min_heapify(self,pos):
		#pdb.set_trace()
		if self.isleaf(pos)==False:
			if self.heap[pos]>self.heap[self.leftchld(pos)] or self.heap[pos]>self.heap[self.rghtchld(pos)]:
				if self.heap[self.leftchld(pos)]<self.heap[self.rghtchld(pos)]:
					self.swapy(pos,self.leftchld(pos))
					self.min_heapify(self.leftchld(pos))
				else:
					self.swapy(pos,self.rghtchld(pos))
					self.min_heapify(self.rghtchld(pos))
					
	
	def insert(self,ele):
		
		self.size+=1
		self.heap[self.size]=ele
		curr=self.size
		while(self.heap[curr]<self.heap[self.parent(curr)]):
			self.swapy(curr,self.parent(curr))
			curr=self.parent(curr)
			
			
	def min(self):
		pos=self.size/2
		for k in range(pos,1,-1):
			self.min_heapify(k)
		
	
	def delete(self):
		#pdb.set_trace()
		tmp=self.heap[self.front]
		self.heap[self.front]=self.heap[self.size]
		self.heap[self.size]=None
		self.size-=1
		self.min_heapify(self.front)
		return tmp
		
	def printy(self):
		for m1 in range(1,(self.size/2)+1):
			print "parent is->",self.heap[m1]
			print "left child is->",self.heap[2*m1]
			print "right child is->",self.heap[2*m1+1]
			
		
			
min=Min_heap(7)
min.insert(4)
min.insert(9)
min.insert(3)
min.insert(10)
min.insert(12)
min.insert(1)
min.min()
print min.delete()	
min.printy()
	