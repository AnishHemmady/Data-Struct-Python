import pdb
class Node:
	def __init__(self,dat):
		self.data=dat
		self.next=None
		self.prev=None

def create_stck():
	stack=[]
	return stack
	
	
def is_empty(stck):
	if len(stck)==0:
		return True
	return False

def pops(stck):
	if is_empty(stck)==False:
		new_nde=stck.pop()
		new_nde=Node(new_nde)
		return new_nde
		
def pops2(stck):
	if is_empty(stck)==False:
		new_nde=stck.pop()
		return new_nde
	
	
def top(stck):
	if is_empty(stck)==False:
		return stck[-1]
	
def push(stck,ele):
	stck.append(ele)
	
def dbly(s1,s2):
	#pdb.set_trace()
	top1=top(s1)
	while is_empty(s1)==False:
		nde=pops(s1)
		if len(s2)<1:
			push(s2,nde)
		else:
			top2=top(s2)
			push(s2,nde)
			top2.prev=top(s2)
	
	head=top(s2)
			
	while is_empty(s2)==False:
		
		nde=pops2(s2)
		top3=top(s2)
		nde.next=top3
		tail=nde
		
	curr=head
	while curr!=None:
		print curr.data
		curr=curr.next
		
	curr=tail
	while curr!=None:
		print curr.data
		curr=curr.prev
		
		
s1=create_stck()
s2=create_stck()
push(s1,1)
push(s1,2)
push(s1,3)
push(s1,4)
dbly(s1,s2)