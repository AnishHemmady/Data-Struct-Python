import pdb
class Node:
	def __init__(self,new_dat):
		self.data=new_dat
		self.next=None
		
class Linkdlst:
	def __init__(self):
		self.head=None
	
	def add(self,dat):
		if self.head==None:
			self.head=Node(dat)
		else:
			curr=self.head
			while(curr.next!=None):
				curr=curr.next
			curr.next=Node(dat)
			
	def printy(self):
		curr=self.head
		while(curr!=None):
			print curr.data
			curr=curr.next
	
	def recursve_invrt(self):
		if self.head==None:
			return "not found"
		else:
			curr=self.head
			self.recursv(curr)
		
		curr=self.head
		while curr!=None:
			print curr.data
			curr=curr.next
			
	def recursv(self,curr):
		#pdb.set_trace()
		if curr.next==None:
			self.head=curr
			return 
		else:
			self.recursv(curr.next)
			prev=curr
			nxt_ele=prev.next
			nxt_ele.next=prev
			prev.next=None
			
		
lkd=Linkdlst()
lkd.add(1)
lkd.add(2)
lkd.add(3)
lkd.printy()
lkd.recursve_invrt()


"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def recur_revrse(heady):
    if heady.next==None:
        head=heady
        return head
    else:
        head=recur_revrse(heady.next)
        prev=heady
        actul_ele=prev.next
        actul_ele.next=prev
        prev.next=None
        return head
        
        
        
        
def ReversePrint(head):
    if head==None:
        return None
    else:
        hd=recur_revrse(head)
        while hd!=None:
            print hd.data
            hd=hd.next
       
    
 
