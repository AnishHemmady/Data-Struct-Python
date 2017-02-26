'''
Quicksort
'''
import pdb
def partn(a,strt,end):
	#pdb.set_trace()
	pivt=a[end]
	k=strt
	for m in range(strt,end):
		if a[m]<=pivt:
			a[m],a[k]=a[k],a[m]
			k+=1
	a[k],a[end]=a[end],a[k]
	return k
	
def quicksort(inp,strty,endy):
	#pdb.set_trace()
	
	if strty<endy:
		indx=partn(inp,strty,endy)
		quicksort(inp,strty,indx-1)
		quicksort(inp,indx+1,endy)
		
	return inp
		
arry=[2,1,0,8,9,4,3]
print quicksort(arry,0,len(arry)-1)


'''
O(N) 
'''
def k_smllst(arry,strty,endy,fnd):
	if fnd>0 and fnd<=endy-strty+1:
		indx=partn(arry,strty,endy)
		if indx-strty==fnd-1:
			return arry[indx]
		elif indx-strty>fnd-1:
			return k_smllst(arry,strty,indx-1,fnd)
		else:
			return k_smllst(arry,indx+1,endy,fnd-indx+strty-1)

print k_smllst(arry,0,len(arry)-1,6)