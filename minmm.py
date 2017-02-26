'''
Minimum cost
'''
import pdb

R=3
C=3

def min(x,y,z):
	#pdb.set_trace()
	if x<y:
		if x<z:
			return x
		else:
			return z
			
	else:
		if y<z:
			return y
		else:
			return z

def minm(cost,m,n):
	#pdb.set_trace()
	tc = [[0 for x in range(C)] for x in range(R)]

	tc[0][0] = 1

	# Initialize first column of total cost(tc) array
	for i in range(1, m+1):
		tc[i][0] = 1

	# Initialize first row of tc array
	for j in range(1, n+1):
		tc[0][j] = 1

	# Construct rest of the tc array
	for i in range(1, m+1):
		for j in range(1, n+1):
			tc[i][j] =  tc[i-1][j]+tc[i][j-1]

	return tc[m][n]
	
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minm(cost, 2, 2))