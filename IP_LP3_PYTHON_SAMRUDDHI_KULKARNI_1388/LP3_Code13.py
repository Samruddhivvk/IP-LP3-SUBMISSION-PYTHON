#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''
Code 13
Write a Python program to count the number of students of the individual class.
'''
def count_strength(classes):
    d={}
    for i in classes:
        if i[0] in d:
            d[i[0]]=d[i[0]]+1
        else:
            d[i[0]]=1
    d={key: value for key, value in sorted(d.items(), key=lambda item: item[1],reverse=True)}
    print(d)
classes = []
n=int(input())
for i in range(n):
    clas=input()
    cnt=input()
    tp=(clas,cnt)
    classes.append(tp)
count_strength(classes)


'''OUTPUT:
6
V
1
VI
1
V
2
VI
2
VI
3
VII
1
{'VI': 3, 'V': 2, 'VII': 1}
'''




