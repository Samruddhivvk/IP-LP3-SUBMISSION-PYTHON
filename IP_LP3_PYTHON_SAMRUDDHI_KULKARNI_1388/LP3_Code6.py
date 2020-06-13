#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
Code 6
Given a matrix of size m*n, m denotes the row starting with index 0 and n denotes the
column starting with index 0.
The matrix will hold distinct integers as elements.
We need to find a distinct number of positional elements which are either the minimum
or maximum in their corresponding row or column.
Please return -1 if any row or any column has multiple minimum or maximum
elements.
'''
import numpy as np
m=int(input())
n=int(input())
matrix=[[0 for i in range(n) ] for j in range(m)]
for i in range(0,m):
    for j in range(0,n):
        matrix[i][j]=int(input())
matrix=np.array(matrix)
#print(matrix)
arr=[]
for i in range(0,m):
    row=matrix[i][0:n]
    #print("row",row)
    mini_col=min(row)
    max_col=max(row)
    #print(mini_col,max_col)
    if(mini_col not in arr):
        arr.append(mini_col)
    if(max_col not in arr):
        arr.append(max_col)
    #print(arr)
for i in range(0,n):
    col=matrix[:,i]
    #print("col",col)
    mini_row=min(col)
    max_row=max(col)
    #print(mini_row,max_row)
    if(mini_row not in arr):
        arr.append(mini_row)
    if(max_row not in arr):
        arr.append(max_row)
    #print(arr)
print(len(arr))


'''OUTPUT:
3
3
1
3
4
5
2
9
8
7
6
7
'''



