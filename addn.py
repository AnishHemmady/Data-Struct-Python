'''
addition without using + operaror
'''

def addn(a,b):
	if b==0:
		return a
	else:
		sum=a^b
		carry=(a&b)<<1
		return addn(sum,carry)
		
		
print addn(23,56)

'''
trailing zeros in factorial
'''
import pdb
def multpl(inp):
	#pdb.set_trace()
	count=0
	if inp<0:
		print "its cant be found"
	else:
		num=inp
		i=5
		while(num/i>0):
			count+=num/i
			i*=5
		return count
		
		
print multpl(26)


'''
2 lines in cartesian plane determine wjether it will intersect or not.
'''
class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		
		
class LL:
	def __init__(self):
		self.head=None
		
	def add_nde(self,new_dat):
		self.nw=new_dat
		new_nde=Node(self.nw)
		if self.head==None:
			self.head=new_nde
		else:
			curr=self.head
			while curr.next!=None:
				curr=curr.next
			curr.next=new_nde
			
			
	def delete_nde(self,del_nde):
		#pdb.set_trace()
		self.delndy=del_nde
		if self.head==None:
			return "cant delete"
		else:
			found=False
			curr=self.head
			prev=self.head
			while curr!=None and found!=True:
				if curr.data==self.delndy:
					found=True
					if curr==self.head:
						self.head=curr.next
					else:
						prev.next=curr.next
				else:
					prev=curr
					curr=curr.next
					
	def fnd_mid(self):
		slow=self.head
		fast=self.head
		while fast!=None:
			fast=fast.next
			if fast!=None and fast.next!=None:
				slow=slow.next
				fast=fast.next
		return slow
		
	def revrse_it(self):
		#pdb.set_trace()
		mid=self.fnd_mid()
		secnd_head=mid.next
		mid.next=None
		mid.data=None
		prevnde=Node(None)
		nxtnde=Node(None)
		curr=secnd_head
		while curr!=None:
			nxtnde=curr.next
			curr.next=prevnde
			prevnde=curr
			curr=nxtnde
		return prevnde
		
	def chck_pali(self):
		#pdb.set_trace()
		secnd_nde=self.revrse_it()
		rev_head=secnd_nde
		curr=self.head
		is_itpali=True
		while rev_head!=None and curr!=None:
			if rev_head.data==curr.data:
				rev_head=rev_head.next
				curr=curr.next
			else:
				is_itpali=False
				break
				
		if is_itpali==True:
			return "its palindrome"
		else:
			return"its not palindrome"
			
	def fnd_nth_frmlst(self,n):
		self.n=n
		count=0
		slw_ptr=self.head
		fst_ptr=self.head
		while(count<self.n and fst_ptr.next!=None):
			fst_ptr=fst_ptr.next
			count+=1
		while fst_ptr!=None:
			slw_ptr=slw_ptr.next
			fst_ptr=fst_ptr.next
		return slw_ptr.data

			
		
				
		
	
L=LL()
L.add_nde(1)
L.add_nde(2)
L.add_nde(3)
L.add_nde(4)
L.add_nde(5)
#L.delete_nde(1)
#L.delete_nde(10)
#print L.chck_pali()
print L.fnd_nth_frmlst(4)				
		
			
'''
fndng prime nos and factors and divisors of numbers
'''


	


			

			