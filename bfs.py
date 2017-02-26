'''
BFS IMPLEMENTED BY ANISH IN PYTHON
'''
import pdb
import Queue
from Queue import Queue
class bfs:
	def __init__(self):
		self.level={}
		self.parent={}
		
class graph:
	#pdb.set_trace()
	def __init__(self):
		self.adjcncy_lst={
        'a':['b','c'],
		'b':['a','d'],
		'c':['d','e'],
		'd':['e'],
		'e':['d']
        }
		
	def add_edge(self,u,v):
		if self.adjcncy_lst[u] is None:
			self.adjcncy_lst[u]=[]
		self.adjcncy_lst[u].append(v)
		print self.adjcncy_lst
		
		
	def bfs(self,s):
		#pdb.set_trace()
		t=bfs()
		t.parent={s:None}
		t.level={s:0}
		q=Queue()
		q.enqueue(s)
		while q.see()!=[]:
			ele=q.dequeue()
			for x in self.adjcncy_lst[ele]:
				if x not in t.level:
					t.parent[x]=ele
					t.level[x]=t.level[ele]+1
					q.enqueue(x)
		return t.parent,t.level

class dfs:
	def __init__(self,s):
		self.parent={s:None}
		self.level={}
		self.adjcncy_lst={
        'a':['b','c'],
		'b':['a','d'],
		'c':['c'],
		'd':['d'],
		'e':['e']
        }
	def dfs_vst_jst_prsnt_nde_neighbrs(self,s):
		#d=bfs()
		#pdb.set_trace()
		self.x=s
		#d.level={s:0}
		for v in self.adjcncy_lst[self.x]:
			if v not in self.parent:
				self.parent[v]=self.x
				self.dfs_vst_jst_prsnt_nde_neighbrs(v)
			
		return self.parent
		
	#def dfs_specl_vst_all_ndes(self,)
gr=graph()
#print gr.bfs('a')
#print gr.dfs_vst_jst_prsnt_nde_neighbrs('a')
#gr.add_edge('1','10')
df=dfs('a')
print df.dfs_vst_jst_prsnt_nde_neighbrs('a')