'''
Insertion sort 
'''
import pdb
def insrtn_srt(inp):
	inp_arry=inp
	leng=len(inp_arry)
	#pdb.set_trace()
	for k in range(0,leng):
		while k>0 and inp_arry[k-1]>inp_arry[k]:
				temp=inp_arry[k-1]
				inp_arry[k-1]=inp_arry[k]
				inp_arry[k]=temp
				k=k-1
				
			
				
	return inp_arry
	
print insrtn_srt([200,1000,20,1,1,4])