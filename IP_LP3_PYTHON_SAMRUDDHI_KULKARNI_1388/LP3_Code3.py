#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
Code 3
You are given n-words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of the
appearance of the word. See the sample input/output for clarification.
'''
n=int(input())
d={}
for i in range(n):
    word=input()
    if(word not in d):
        d[word]=1
    else:
        d[word]=d[word]+1
print(len(d))
for j in d.keys():
    print(d[j],end=" ")


'''OUTPUT:
4
bcdef
abcdefg
bcde
bcdef
3
2 1 1 
'''



