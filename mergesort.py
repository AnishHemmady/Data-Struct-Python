'''
merge sort
'''
import pdb
global swapcount
swapcount=0
def merge(lft,rght,old_lst):
	#pdb.set_trace()
	lefty=lft
	rghty=rght
	leng1=len(lefty)
	leng2=len(rghty)
	k=0
	i=0
	j=0
	global swapcount
	while(i<leng1 and j<leng2):
		if lefty[i]<rghty[j]:
			old_lst[k]=lefty[i]
			k+=1
			i+=1
			
		else:
			old_lst[k]=rghty[j]
			k+=1
			j+=1
			swapcount+=1
	
	while(i<leng1):
		old_lst[k]=lefty[i]
		i+=1
		k+=1
	while(j<leng2):
		old_lst[k]=rghty[j]
		j+=1
		k+=1
def mergesort(inp):

	#pdb.set_trace()
	input=inp
	leng=len(input)
	if leng<2:
		return
	mid=leng/2
	left=input[:mid]
	right=input[mid:]
	mergesort(left)
	mergesort(right)
	merge(left,right,input)
	
	return input
	
print mergesort([1,4,])
print swapcount			
