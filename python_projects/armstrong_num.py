# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:46:06 2020

@author: Ashish chaudhary
"""

str_num=input("Enter the  number: ")     # number is inp as string type
order=len(str_num)                       # number of digit in string number
num=int(str_num)                         # string number is converted to integer type(used on line24)
digits_list=[]                            #empty list 
summ=0

for i in range (0, order):
    a=int(str_num[i])             # each digit in string number is converted to int type seperately
    b=pow(a,order)                # each digit now cubed seperately
    print("power of",order,"to digit",i+1,"=",b)
    digits_list.append(b)         #cubed digits are appended into empty list
   
for j in digits_list:
    summ+=j                       #all cubed digits are being added which already appeded into list
print("-"*30)    
print("The sum of digits ====>",summ) 

if summ==num:
    print("It is an armstrong number")
else:
    print("it is not an armstrong number")