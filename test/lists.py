##implement mergesort

class Node:
    	def __init__(self,initdata):
        	self.data = initdata
        	self.next = None
		self.prev = None

class Linkedlist:
	def __init__(self):
		print "Create a list"

	def create(self,k):
		self.head = Node(k)
		self.tail=self.head
		
	def printlist(self):
		k=self.head
		while (k != None):
			print k.data
			k =k.next

	def append(self,k):
		M = Node(k)
		M.next = self.head
		self.head = M


	def createlist(self,arr=[2,1,3,1,4]):
		self.head = Node(arr[0])
		self.tail=self.head	
		for i in range(1,len(arr)):
			self.append(arr[i])

	def findminimum(self):
                k=self.head
                min = 1000000
                while (k != None):
                        if (k.data <= min):
                                min=k.data
                        k =k.next
                return min


	def size(self):
                k=self.head
                count = 0
                while (k != None):
                        count = count + 1
			k =k.next
                return count

	def search(self,num):
                k=self.head
                while ((k != None) and (k.data != num)):
                        k =k.next
                if (k != None):
			return k
		else:
			print "Not found"

	def delete(self,num):
		if ((self.head.next ==None) and (self.head.data == num)):
			self.head =None
			return	
	
		k=self.head
		m=k
		count = 0
		while (k.data == num):     
                 	count = count +1
			self.head = k.next
			k=k.next			
	
		while (k.next != None):
			m=k
			k=k.next
			if (k.data == num) :
                        	count = count + 1
				m.next=k.next
                print str(count)+"items deleted"


	def reverse(self):
		current=self.head
		self.tail=self.head
		behind=None
		behinder=None
		if (self.head==None):
			return
		elif(self.head.next == None):
			return
		elif(self.head.next.next == None):
			temp=self.head.next
			self.head.next.next=self.head
			self.head.next=None
			self.head=temp
		else:
			behind=current
			current=current.next
			behind.next=None
			temp=current.next
			while (temp != None):
				temp=current.next
				current.next=behind
				behind=current
				self.head=current
				current= temp
						


	def merge(self,list1,list2):
		if (list1==None):
			return list2
		elif (list2==None):
			return list1
		else:
			start1=list1.head
			start2=list2.head
			if (start1.data>start2.data):
				self.create(start2.data)
				start2=start2.next
			else:
				self.create(start1.data)
				start1=start1.next
			while(not((start1== None) and (start2 == None))):
				if (start1==None):
					self.append(start2.data)
					start2=start2.next
				elif(start2==None):
					self.append(start1.data)
					start1=start1.next
				elif(start1.data>start2.data):
					self.append(start2.data)
					start2=start2.next
				else:
					self.append(start1.data)
					start1=start1.next
			self.reverse()
			return self	
	
	def mergesort(self,list):
		if (list==None):
			n=0
			return list
		else:
			n=list.size()
			if (n<=1):
				return list
			else:
				runner=list.head
				k=Linkedlist()
				k.create(list.head.data)
				l=Linkedlist()			
				for i in range(0,(n-1)/2):
					runner=runner.next
					k.append(runner.data)
				l.create(runner.next.data)
				runner=runner.next
				while (runner.next!=None):
					runner=runner.next
					l.append(runner.data)
				
				k.reverse()
				l.reverse()
				k1=self.mergesort(k)
				l1=self.mergesort(l)
				W=Linkedlist()
				moo=W.merge(l1,k1)
				return moo
				
class Doublylinkedlist:
        def __init__(self):
                print "Create a doubly list"

        def create(self,k):
                self.head = Node(k)
		self.tail = self.head
		
        def printlist(self):
                k=self.head
                while (k != None):
                        print k.data
                        k =k.next

        def append(self,k):
                M = Node(k)
                M.next = self.head
		self.head.prev=M
                self.head = M
		

        def createlist(self,arr=[2,1,3,1,4]):
                self.head = Node(arr[0])
                self.tail = self.head
		for i in range(1,len(arr)):
                        self.append(arr[i])


	def printlistrev(self):
                k=self.tail
                while (k != None):
                        print k.data
                        k =k.prev

	def findminimum(self):
		k=self.head
		min = 100
		while (k != None):
                        if (k.data <= min):
				min=k.data	
			k =k.next
		return min

	def size(self):
		k=self.head
                count = 0
                while (k != None):
                        count = count + 1
			k =k.next 
                return count


	def find(self,num):
		k=self.head
		while ((k != None) and (k.data != num)):
			k =k.next
		return k
				

	def delete(self,node):
		if (node==None):
			pass
		elif ((node.prev ==None) and (node.next ==None)):
			self.head =None
			return
		elif (node.prev ==None):
			self.head =node.next
			self.head.prev=None
		elif (node.next ==None):
			self.tail =node.prev
			self.tail.next=None
		else:
			node.prev.next=node.next
			node.next.prev=node.prev


	def deleteall(self,num):
		while(self.find(num) !=None):
			m=self.find(num)
			self.delete(m)		

class Ordered_doublylinkedList:
	def __init__(self):
                print "Create a doubly list"

        def create(self,k):
                self.head = Node(k)
                self.tail = self.head

        def printlist(self):
                k=self.head
                while (k != None):
                        print k.data
                        k =k.next

        def append(self,k):
                M = Node(k)
		runner=self.head
		while ((runner.data < k) and (runner.next != None)):
			runner=runner.next
		
		print runner.data	
		if (runner.data<k):
			runner.next=M
			M.prev=runner
			self.tail=M
		
		else:
			if(runner.prev == None):
				M.next=runner
				runner.prev=M
				self.head=M
			else:
				runner.prev.next=M
				M.prev=runner.prev
				M.next=runner
				runner.prev=M	
		'''
		tail=self.head
		while (tail.next != None):
			tail=tail.next	
		'''
				

        def createlist(self,arr=[2,1,3,1,4]):
                self.head = Node(arr[0])
                self.tail = self.head
                for i in range(1,len(arr)):
                        self.append(arr[i])


	def printlistrev(self):
                k=self.tail
                while (k != None):
                        print k.data
                        k =k.prev


        def findminimum(self):
                k=self.head
                min = 100000000
                while (k != None):
                        if (k.data <= min):
                                min=k.data
                        k =k.next
                return min




class Ordered_singlylinkedlist:
	def __init__(self):
		print "Create a list"

	def create(self,k):
		self.head = Node(k)
	
	def printlist(self):
		k=self.head
		while (k != None):
			print k.data
			k =k.next

	def createlist(self,arr=[2,1,3,1,4]):
		self.head = Node(arr[0])
		for i in range(1,len(arr)):
			self.append(arr[i])

	def findminimum(self):
                k=self.head
                min = 1000000
                while (k != None):
                        if (k.data <= min):
                                min=k.data
                        k =k.next
                return min


	def size(self):
                k=self.head
                count = 0
                while (k != None):
                        count = count + 1
			k =k.next
                return count

	def search(self,num):
                k=self.head
                while ((k != None) and (k.data != num)):
                        k =k.next
                if (k != None):
			return k
		else:
			print "Not found"

	def delete(self,num):
		if ((self.head.next ==None) and (self.head.data == num)):
			self.head =None
			return	
	
		k=self.head
		m=k
		count = 0
		while (k.data == num):     
                 	count = count +1
			self.head = k.next
			k=k.next			
	
		while (k.next != None):
			m=k
			k=k.next
			if (k.data == num) :
                        	count = count + 1
				m.next=k.next
                print str(count)+"items deleted"




 	def append(self,k):
                M = Node(k)
		runner=self.head
		behind=None
		while ((runner.data < k) and (runner.next != None)):
			behind=runner
			runner=runner.next
		
		if (runner.data<k):
			runner.next=M
			self.tail=M
		
		else:
			if(behind == None):
				M.next=runner
				self.head=M
			else:
				behind.next=M
				M.next=runner
		
