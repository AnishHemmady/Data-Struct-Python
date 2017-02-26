import pdb
A=[0,1,0,2,0,2,1,0]
pdb.set_trace()
leng=len(A)
hghr=leng-1
nxt=0
k=0
while k<=hghr:
	if A[k]==0:
		if A[k]==A[nxt]:
			nxt+=1
			k+=1
		else:
			A[k],A[nxt]=A[nxt],A[k]
			nxt+=1
			k+=1
	elif A[k]==2:
		if A[k]==A[hghr]:
			hghr-=1
		else:
			A[k],A[hghr]=A[hghr],A[k]
			hghr-=1
		
	else:
		k+=1
			
print A	
	
		