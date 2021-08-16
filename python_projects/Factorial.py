# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:37:10 2020

@author: Ashish chaudhary
"""

def factorial(n): 
	if n < 0: 
		return 0
	elif n == 0 or n == 1: 
		return 1
	else: 
		fact = 1
		while(n > 1): 
			fact *= n 
			n -= 1
		return fact 
#alternative single lined program...
#          return 1 if (n==1 or n==0) else n * factorial(n - 1);



num = int(input("Enter the number:")); 
print("Factorial of",num,"is", factorial(num)) 
