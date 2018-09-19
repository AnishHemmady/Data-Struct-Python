'''
Circular Queue
'''
import pdb
class Circ_q:
	def __init__(self,len):
		self.lmt=len-1
		self.queue=[]
		self.frnt=-1
		self.rear=-1
		
	def dequeue(self):
		if self.frnt==-1:
			return "queue is empty"
		else:
			item=self.queue[self.frnt]
			self.frnt+=1
			self.queue=self.queue[1:]
			if self.frnt==self.rear:
				self.frnt=-1
				self.rear=-1
			
			if self.frnt>self.lmt:
				loc=(self.frnt%self.lmt)-1
				self.frnt=loc
				self.queue=self.queue[1:]
				
			print self.queue
			
			return item

	def enqueue(self,itm):
	
		if self.rear==-1:
			self.frnt=0
			self.rear=0
			self.queue.append(itm)
			
		else:
			self.rear+=1
			pdb.set_trace()
			if self.rear>self.lmt:
				loctn=(self.rear%self.lmt)-1
				self.rear=loctn
				if self.rear<self.frnt:
					self.queue[self.rear]=itm
				else:
					return "queue is full"
			else:
				if self.rear==self.frnt:
					print "its full"
				else:
					self.queue.append(itm)
					
		print self.queue
					
q=Circ_q(4)
q.enqueue('a')
q.enqueue('v')
q.enqueue('c')
q.enqueue('l')
#print q.enqueue('m')
print q.dequeue()
print q.enqueue('m')
print q.enqueue('k')
print q.enqueue('p')
