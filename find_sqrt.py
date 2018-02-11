#babylonian method
def find_sqrt(no):
	e=0.00001
	x=no
	y=1
	while(x-y)>e:
		x=(x+y)/2
		y=no/x
	x=round(x,2)
	print(x)
	
find_sqrt(15)