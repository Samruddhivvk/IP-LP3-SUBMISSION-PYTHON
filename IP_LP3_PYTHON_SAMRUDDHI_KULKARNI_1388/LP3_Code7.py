#!/usr/bin/env python
# coding: utf-8

# In[19]:


'''
Code 7
Write a Python program to find the first appearance of the substring 'not' and 'poor' from
a given string, if 'not' follows the 'poor', replace the whole 'not'...' poor' substring with
'good'. Return the resulting string.
'''
import re
def remove_sub(string):
    string_list=string.split()
    string=re.sub('not[^>]+poor!', 'good!', string)
    return string
string=input()
remove_sub(string)


'''OUTPUT:
'The lyrics is not that poor!'
"'The lyrics is good!'"
'''




