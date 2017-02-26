def partn(a,p,r):
	i=p-1
	pivt=a[r]
	for j in range(p,r):
		if a[j]<=pivt:
			i+=1
			a[i],a[j]=a[j],a[i]
			#temp=a[i]
			#a[i]=a[j]
			#a[j]=temp
	a[i+1],a[r]=a[r],a[i+1]
	return i+1



def quick_srt(a,p,r):
	if p<r:
		q=partn(a,p,r)
		quick_srt(a,p,q-1)
		quick_srt(a,q+1,r)
		
lst=[12,8,4,2,1,0]
quick_srt(lst,0,len(lst)-1)
print lst