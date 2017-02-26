'''
Linkedlist by Anish
Singly linked list and doubly linked list with special ansi
oops (0ops) sorry anish features
'''
import pdb
class Node:
	def __init__(self,data):
		self.prev=None
		self.data=data
		self.next=None
		
	def grab_data(self):
		return self.data
	
	def grab_nxt(self):
		return self.next

	def set_data(self,dat):
		self.data=dat
	
	def set_nxt(self,nxt):
		self.next=nxt
		
	def set_prev(self,prev):
		self.prev=prev
		
	def grab_prev(self):
		return self.prev
		
class LL:
	def __init__(self):
		self.head=None
		
	def insert(self,new_dat):
		nde=Node(new_dat)
		if self.head==None:
			self.head=nde
		else:
			#pdb.set_trace()
			current=self.head
			while(current.grab_nxt()!=None):
				current=current.grab_nxt()
			current.set_nxt(nde)
			nde.set_prev(current)
			
	def trvrse_bckwrd(self):
		self.rev_trv=[]
		self.nrml=[]
		if self.head==None:
			return "nothing present"
		else:
			current=self.head
			self.nrml.append(current.data)
			while current.grab_nxt()!=None:
				current=current.grab_nxt()
				self.nrml.append(current.data)
			self.rev_trv.append(current.data)
			#pdb.set_trace()
			while current.grab_prev()!=None:
				current=current.grab_prev()
				self.rev_trv.append(current.data)
			#self.rev_trv.append(current.data)
			return self.rev_trv,self.nrml
			
			
	def check_size(self):
		hd=self.head
		count=1
		while hd.grab_nxt()!=None:
			count+=1
			hd=hd.grab_nxt()
		return count
		
			
			
	def printy(self):
		self.listy=[]
		if self.head==None:
			return "sorry no elements"
		else:
			strt=self.head
			self.listy.append(strt.data)
			while(strt.grab_nxt()!=None):
				strt=strt.grab_nxt()
				self.listy.append(strt.grab_data())
			#self.listy.append(strt.grab_data())
			return self.listy
			
	def delete(self,ele):
		#pdb.set_trace()
		self.ele=ele
		if self.head==None:
			return "No elements present idiot"
		else:
			begin=self.head
			prev=None
			found=False
			while begin!=None and found==False:
				if begin.grab_data()==self.ele:
					found=True
				else:
					prev=begin
					begin=begin.grab_nxt()
			if prev==None:
				self.head=begin.grab_nxt()
				self.head.set_prev(prev)
			if prev!=None:
				prev.set_nxt(begin.grab_nxt())
				new_plce=begin.grab_nxt()
				new_plce.set_prev(prev)
			print self.head.next.data
			print self.head.prev
				#prev.set_prev()
				#begin.set_prev(prev)
	
	def search(self,key):
		self.fnd=key
		begin=self.head
		found=False
		while begin!=None and found==False:
			if begin.grab_data()==self.fnd:
				found=True
				return "element found"
			else:
				begin=begin.grab_nxt()
		if found==False:
			return "element not found"
				
		
	def check_is_itPali(self):
		import math
		#pdb.set_trace()
		size=self.check_size()
		if size==0:
			return "not valid size"
		mid=math.ceil(size/2.0)
		curr=self.head
		heady=self.head
		while(curr.grab_nxt()!=None):
			curr=curr.grab_nxt()
		curr.set_nxt(heady)
		heady.set_prev(curr)
		count=0
		#so our circular linked list is ready
		while(count<mid):
			if curr.data==heady.data:
				pass
				curr=curr.grab_prev()
				heady=heady.grab_nxt()
				count+=1
			else:
				return "its not palindrome"
				#break
		return "its pali"
		
			

def main():
	l=LL()
	l.insert('m')
	l.insert('m')
	l.insert('a')
	l.insert('l')
	l.insert('a')
	l.insert('y')
	l.insert('a')
	l.insert('l')
	l.insert('a')
	l.insert('m')
	l.delete('m')
	#print l.search(3)
	print l.printy()
	print l.trvrse_bckwrd()
	print l.check_is_itPali()
	
if __name__=='__main__':
	main()

