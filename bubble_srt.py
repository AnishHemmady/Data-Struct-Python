
def bubble(inp):
	for i in range(0,len(inp)-1):
		for j in range(0,len(inp)-1-i):
			if inp[j]>inp[j+1]:
				inp[j],inp[j+1]=inp[j+1],inp[j]

inp=[2,6,7,3,1]
bubble(inp)
print inp