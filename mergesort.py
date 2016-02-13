##implement mergesort

import math

class Mergesort():
	def __init__(self):
		self.array1=[]
		self.array=[]
		k=input("Enter array legth:")
		for i in range(0,k):
			m=input("Enter number")
			self.array.append(m)
	
	def add_array(self):
                k=input("Enter array legth:")
                for i in range(0,k):
                        m=input("Enter number")
                        self.array1.append(m)
		

	def show(self):
		print self.array


	def mergesort(self,array):
		n=len(array)
		if (n<=1):
			return array
		start=0
		mid = len(array)/2
		end = len(array)             
		k= self.mergesort(array[start:mid])
		m= self.mergesort(array[mid:end])
		return 	self.merge(k,m)


	def merge(self,array1=[1,3,4,9],array2=[2,5,9,11]):
		m=len(array1)		
		n=len(array2)
		output=[]
		a=0
		b=0
		for i in range(0,m+n):
			if (a<m and b<n):
				if (array1[a]>array2[b]):
					output.append(array2[b])
					b=b+1
				else:
					output.append(array1[a])
					a=a+1	
			elif (b==n):
				output.append(array1[a])
				a=a+1
			else:
				output.append(array2[b])
                               	b=b+1
		return output



k=Mergesort()
print k.mergesort([1,2,3,4,5,6,7,8])
