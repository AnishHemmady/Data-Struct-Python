import pdb

def insrt_below(stack,ele):
	pdb.set_trace()
	if is_chck_empty(stack)==True:
		push(stack,ele)
	else:
		temp=pops(stack)
		insrt_below(stack,ele)
		push(stack,temp)
		


def reverse(stack):
	pdb.set_trace()
	if is_chck_empty(stack)==False:
		new=pops(stack)
		reverse(stack)
		insrt_below(stack,new)

def create_stck():
	stack=[]
	return stack
	
def push(stack,ele):
	stack.append(ele)
	
def topy(stack):
	print stack[-1]
	
def is_chck_empty(stack):
	if len(stack)==0:
		return True
	return False
	
def pops(stack):
	if is_chck_empty(stack)==False:
		return stack.pop()
		
		
	
def peek(stack):
	top=stack[-1]
	return top
	
def printy(stack):
	print stack
	
stck=create_stck()
push(stck,1)
push(stck,2)
push(stck,3)
push(stck,4)
print stck
reverse(stck)
printy(stck)
topy(stck)


