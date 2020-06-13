#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''
Code 4
Little Robert likes mathematics. Today his teacher has given him two integers and
asked to find out how many integers can divide both the numbers. Would you like to
help him in completing his school assignment?
'''
num1=int(input())
num2=int(input())
count=0
mini=min(num1,num2)
if(num1==0):
    print(0)
else:
    for i in range(1,(mini+1)):
        if(num1%i==0 and num2%i==0):
            count=count+1
    print(count)


'''OUTPUT:
12
10
2
'''




