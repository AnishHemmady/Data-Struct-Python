import pdb
import networkx as nx
from matplotlib import pyplot as plt
d = {}
g = nx.Graph()
wfile = open('laddr.txt','r')
# create buckets of words that differ by one letter

for line in wfile:
	word = line[::].rstrip()
	#print word
	for i in range(len(word)):
		bucket = word[:i] + '_' + word[i+1:]
		if bucket in d:
			d[bucket].append(word)
		else:
			d[bucket] = [word]
#pdb.set_trace()			
for bucket in d.keys():
	for word1 in d[bucket]:
		for word2 in d[bucket]:
			if word1 != word2:
				g.add_edge(word1,word2)

print(g.edges())
nx.draw(g)
plt.show()				