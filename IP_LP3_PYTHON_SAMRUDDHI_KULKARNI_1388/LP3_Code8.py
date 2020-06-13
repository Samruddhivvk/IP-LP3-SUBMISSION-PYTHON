#!/usr/bin/env python
# coding: utf-8

# In[12]:


'''
Code 8
Write a Python program to convert temperatures to and from celsius, Fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
Fahrenheit]
'''
import re
temperature=input()
num=list(map(int, re.findall(r'\d+',temperature)))
num=float(num[0])
if('F' in temperature or 'f' in temperature):
    temp= (num - 32) * 5.0/9.0
    print(temperature,"is",int(temp),"in Celcius")
elif('C' in temperature or 'c' in temperature):
    temp=(9.0/5.0) * num + 32
    print(temperature,"is",int(temp),"in Fahrenheit")


'''OUTPUT:
60C
60C is 140 in Fahrenheit
'''




