#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
Code 12
Write a Python program to get a week number.
'''
import datetime
from datetime import date
dt=[]
for i in range(3):
    dt.append(int(input()))
print(date(dt[0],dt[1],dt[2]).isocalendar()[1])



'''OUTPUT:
2020
1
8
2
'''



