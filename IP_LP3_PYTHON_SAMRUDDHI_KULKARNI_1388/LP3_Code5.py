#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
Code 5
You have given a string. You need to remove all the duplicates from the string.
The final output string should contain each character only once. The respective order of
the characters inside the string should remain the same. You can only traverse the
string at once.
'''
string=input()
unique=""
for i in range(len(string)):
    if(string[i] not in unique):
        unique=unique+string[i]
string=unique
print(string)


'''OUTPUT:
ababacd
abcd
'''




