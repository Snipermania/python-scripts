# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 13:49:53 2020

@author: Ashish chaudhary
"""

def simple_interest(p,t,r): 
	print('The principal is', p) 
	print('The time period is', t) 
	print('The rate of interest is',r) 
	
	si = (p * t * r)/100
	
	print('The Simple Interest is', si) 
	return si 
	
simple_interest(8, 6, 8) 
