#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
Code 9
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
(until n-x>=0).
'''
def summ(num):
    if num<1:
        return 0
    else:
        i=0
        value=0
        while(num-(i*2)>=0):
            value=value+(num-i*2)
            i=i+1
        return value
num=int(input())
summ(num)

'''OUTPUT:
10
30
'''
