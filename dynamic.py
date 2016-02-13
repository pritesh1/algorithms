import numpy as np
import math


class DP():
	
	def __init__(self):
		self.M=[1,2]
		self.weights=[1,1]
		N=21

	# the recurrence relation
	def count(self,remainder):
        	if remainder < 0:
                	return 0
        	if remainder == 0:
                	return 1
        	return sum(self.count(remainder - number) for number in self.M)

	def count_probability(remainder):
        	if remainder < 0:
                	return 0
        	if remainder == 0:
                	return 1
        	return sum((1./7)*(count_probability(remainder - number)) for number in self.M)
	
	def few_coins(self,remainder):
                if remainder <= 0:
                        return 0
		else:	
			min=1000
			print "\n"
			for number in self.M:	
			  	k = self.few_coins(remainder-number)
				if (k< min):
					min=k 
			return min+1

	def knapsack(self,remainder):
                if remainder <= 0:
                        return 0
                else:   
                        min=0
			i=0
			val=00000
                        print "\n"
                        for number in self.M:	   
                                k = self.knapsack(remainder-number)
				if (k>= min):
                                        min=k
					val=self.weights[i]
				i=i+1
                        return min+val


        




