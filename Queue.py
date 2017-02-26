'''
queue implementation
'''
import pdb
class Queue:

	def __init__(self):
		self.listy=[]
		
	def enqueue(self,dat):
		self.listy.append(dat)
		
	def dequeue(self):
		#pdb.set_trace()
		rem=self.listy[0]
		self.listy=self.listy[1:]
		return rem
	def see(self):
		return self.listy
		


if __name__=='__main__':
	main()

