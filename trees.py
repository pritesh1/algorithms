##implement mergesort

class Node:
        def __init__(self,initdata):
                self.data = initdata
                self.left = None
                self.right = None
		self.parent = None

class BST:
        def __init__(self):
                print "Create a tree"
		self.root=None		

        def create(self,k):
                self.root = Node(k)


        def add(self,k):
		M=Node(k)
		self.insert(M)	
				

	def insert(self,k):
		x=self.root
		while (x != None):
			y=x
			if (k.data<x.data):
				x = x.left
			else:
				x=x.right
		k.parent = y
		if (k.data <y.data):
			y.left =k
		else:
			y.right =k
	
	def create_tree(self,list):
		self.create(list[0])
		for i in range(1,len(list)):
			self.insert(Node(list[i]))					

	def printmyself(self):
		self.printsorted(self.root)


	def printsorted(self,node):
		if  (node == None):
			return
		else:
			print node.data	
			self.printsorted(node.left)
			#print node.data
			self.printsorted(node.right)
		

	def search(self,k):
		if (self.root==None):
			return None
		else:
			x=self.root
			while ((x.data!=k) and (x.left!=None) and (x.right!=None)):
				if (x==None):
					return x
				elif (k<x.data):
					x=x.left
					print 1
				elif (k>x.data):
					x=x.right
					print 2
				else :
					print 3

			if (x.data==k):
				return x
			else:
				return None

	
	def search_rec(self,k):
		return self._search(self.root,k)


	def _search(self,x,k):
		if ((x==None)):
			return x
			print 1
		elif (x.data==k):
			return x
			print 2
		else:
			if (k<x.data):
				
                           	return self._search(x.left,k)
		 	else:
				return self._search(x.right,k)

	
	def height(self,node):
		if (node==None):
			return 0
		else:
			return max(1+self.height(node.left),1+self.height(node.right))
		
	def lowtt(self,node):
		if (node==None):
                        return 0
                else:
                        return min(1+self.height(node.left),1+self.height(node.right))		

	def find_minimum(self,node):
		if (node.left==None):
			return node.data
		else:
			return self.find_minimum(node.left)

	def successor(self,node):
		if (node==None):
			return None
		elif(node.right==None):
			return node.parent.data
		else:
			return self.find_minimum(node.right)	



		



	
