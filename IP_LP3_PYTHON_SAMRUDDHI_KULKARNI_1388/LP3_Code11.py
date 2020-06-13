#!/usr/bin/env python
# coding: utf-8

# In[5]:


'''
Code 11
Write a Python program to sort a list of elements using the selection sort algorithm.
'''
size=int(input())
num=[]
for i in range(size):
    num.append(int(input()))
for i in range(0,size):
    for j in range(i+1,size):
        if(num[i]>num[j]):
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)

'''OUTPUT:
9
14
46
43
27
57
41
45
21
70
[14, 21, 27, 41, 43, 45, 46, 57, 70]
'''




