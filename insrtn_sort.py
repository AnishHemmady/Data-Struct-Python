'''
Insertion sort python by anish
insertion sort using recursion-
'''
import pdb
def insrtn_srt(inp):
	#pdb.set_trace()
	inp_arry=inp
	key_ptr=inp_arry[1]
	for i in range(1,len(inp_arry)):
		if key_ptr<inp_arry[i-1]:
			new_arry=swap(i,i-1,inp_arry)
			inp_arry=new_arry
			if i==len(inp_arry)-1:
				break
			key_ptr=inp_arry[i+1]
		else:
			key_ptr=inp_arry[i+1]
			
	return inp_arry
			
def swap(m,k,arry):
	#pdb.set_trace()
	curr_pos=m
	befr_pos=k
	input=arry
	if befr_pos<0:
		befr_pos=0
	else:
		pass
	if input[befr_pos]<=input[curr_pos]:
		return input
	else:
		temp=input[befr_pos]
		input[befr_pos]=input[curr_pos]
		input[curr_pos]=temp
		swap(curr_pos-1,befr_pos-1,input)
		
	return input

print insrtn_srt([1000,50,1,2000000,150,1,3,10,4])


