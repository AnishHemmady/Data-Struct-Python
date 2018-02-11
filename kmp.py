class KMP(object):
#import pdb
	def generate_pattern(self,find_pattern):
	
		i=1
		j=0
		find_pattern=list(find_pattern)
		new_pattern_pos=[None]*len(find_pattern)
		new_pattern_pos[0]=0
		while i<len(find_pattern):
			if find_pattern[i]==find_pattern[j]:
				value=j+1
				new_pattern_pos[i]=value
				j+=1
				i+=1
			else:
				j=j-1
				if j<0:
					j=0
					value=new_pattern_pos[j]
					new_pattern_pos[i]=value
					i+=1
				else:
					new_pos=new_pattern_pos[j]
					j=new_pos
		return new_pattern_pos
	def kmp_search(self,input,pattern):
		new_pattern=self.generate_pattern(pattern)
		i=0
		j=0
		input=list(input)
		while i<len(input) and j<len(new_pattern):
			if input[i]==pattern[j]:
				i+=1
				j+=1
			else:
				if j>0:
					j=new_pattern[j-1]
				else:
					i+=1
		if j==len(new_pattern):
			return True
		return False
	
					
			

k=KMP()
ans=k.kmp_search("abxabcabcaby","abcaby")
print(ans)