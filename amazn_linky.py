import pdb
import math
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.vstd=0

	def grab_data(self):
		return self.data
	def set_nxt(self,nxt):
		self.next=nxt
	def set_data(self,dat):
		self.data=dat
	def grab_nxt(self):
		return self.next
		
class Linkedlist:
	def __init__(self):
		self.head=None
	def add(self,dat):
		new_nde=Node(dat)
		if self.head==None:
			self.head=new_nde
		else:
			curr=self.head
			while(curr.grab_nxt()!=None):
				curr=curr.grab_nxt()
			curr.set_nxt(new_nde)
			
	def printy(self):
		#pdb.set_trace()
		self.new_lst=[]
		curr=self.head
		while curr!=None:
			self.new_lst.append(curr.data)
			curr=curr.grab_nxt()
		return self.new_lst
	
	def check_size(self):
		strt=self.head
		counter=1
		while strt!=None:
			counter+=1
			strt=strt.grab_nxt()
		return counter
		
	def singly_pali(self):
		curr=self.head
		heady=self.head
		county=1
		size=self.check_size()
		stop=math.ceil(size/2.0)
		while county<stop:
			if curr.grab_nxt()==None or (curr.grab_nxt().vstd==1) :
				curr.vstd=1
				new_head=heady.next
				tail=curr
				if heady.data==tail.data:
					pass
				else:
					return "Not palindrome"
				heady=new_head
				county+=1
				curr=new_head
			else:
				curr=curr.grab_nxt()
				
		return "its palindrome"
					
	def specl_func(self):
		#pdb.set_trace()
		curr=self.head
		heady=self.head
		county=1
		size=self.check_size()
		stop=math.ceil(size/2.0)
		while county<=stop:
			if curr.grab_nxt()==None or (curr.grab_nxt().vstd==1) :
				curr.vstd=1
				new_head=heady.next
				tail=curr
				heady.set_nxt(tail)
				if county==stop:
					tail.set_nxt(None)
				else:
					tail.set_nxt(new_head)
				heady=new_head
				#heady=
				county+=1
				curr=new_head
			else:	
				curr=curr.grab_nxt()
		
			
		
list=Linkedlist()
list.add('m')
list.add('a')
list.add('l')
list.add('a')
list.add('y')
list.add('a')
list.add('l')
list.add('a')
list.add('m')

#list.add(5)
#list.add(6)
#list.specl_func()
print list.printy()
print list.singly_pali()

			
			
			
			