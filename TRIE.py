class TrieNode(object):
	def __init__(self):
		self.children={}
		self.endofword=False
		self.freq=1
		
	def add(self,new_char,value):
		self.children[new_char]=value
		
class Trie(object):
	def __init__(self,input=None):
		self.input=input
		self.root=None
		#for longest prefix
		
		
	def load_datastructure(self):
		#pdb.set_trace()
		char_arry=list(self.input)
		if self.root is None:
			self.root=TrieNode()
		current_node=self.root
		while char_arry:
			pop_letter=char_arry.pop(0)
			new_node=current_node.children.get(pop_letter)
			if new_node is None:
				new_node = TrieNode()
				current_node.add(pop_letter,new_node)
				
			current_node=new_node
		current_node.endofword=True
		return "Lock and Loaded"
		
		
	def search(self,word):
		curr=self.root
		char_arry=list(word)
		#pdb.set_trace()
		while char_arry:
			pop_ele=char_arry.pop(0)
			key_present=curr.children.get(pop_ele)
			if key_present==None and curr.endofword!=True:
				return "Not present"
			else:
				curr=key_present
		return "key present"
		
	def pretty(self,d, indent=0):
		for key, value in d.items():
			print('\t' * indent + str(key))
			if isinstance(value, TrieNode):
				self.pretty(value.children, indent+1)
			else:
				print('\t' * (indent+1) + str(value))
				
	def get_longest_prefix(self,word,target_length):
		char_arry=list(word)
		if self.root is None:
			self.root=TrieNode()
		current_node=self.root
		output=[]
		#pdb.set_trace()
		while char_arry:
			pop_letter=char_arry.pop(0)
			new_node=current_node.children.get(pop_letter)
			if new_node is None:
				new_node = TrieNode()
				current_node.add(pop_letter,new_node)
				current_node=new_node
			else:
				new_node.freq+=1
				if new_node.freq==target_length:
					output.append(pop_letter)
				current_node=new_node
		if len(output)>0:
			return output
		
		
				
			

	def longest_prefix(self,inpt_list):
		for word in inpt_list:
			result=self.get_longest_prefix(word,len(inpt_list))
		if result!=None:
			return ("Longest prefix is:{}".format(''.join(result)))
		else:
			return ("Longest prefix was not Found")
			
			
			
#trie=Trie("annish")
#trie=Trie()
#ans=trie.load_datastructure()
#print(ans)
#ans_res=trie.search("ish")
#print(ans_res)
#print(trie.pretty(trie.root.children))
#ans=trie.longest_prefix(["meeeeeeeksforgeeks","keeeeekyyyy","leeeeeks"])
#print(ans)