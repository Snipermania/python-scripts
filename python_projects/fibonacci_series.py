# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:20:14 2020

@author: Ashish chaudhary
"""

n=int(input("Enter the term you want: "))        #which term of fibonacci series you want?
a=[0,1]                                  #first two terms already entered ito list
if n<=0:
   print("invalid input")
elif n==1:
     print("the first term of series is",a[n-1])  
else:
    for i in range(1,(n-1)):    
        a.append(a[i]+a[i-1])
    print(a)                                
    print("the term of series you asked for is",a[n-1])        #nth term of series