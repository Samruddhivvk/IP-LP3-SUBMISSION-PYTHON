#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''
Code 10
Write a Python program to check whether a given a binary tree is a valid binary search
tree (BST) or not.
'''
class Node: 
    def __init__(self, data): 
        self.left = None
        self.right = None
        self.data = data
def checkBST(root): 
    mini_val=root.data
    max_val=root.data
    if root:
        if root.left:
            if root.left.data<mini_val:
                mini_val=root.left.data
                checkBST(root.left)
            else:
                return False
        if root.right:
            if root.right.data>max_val:
                max_val=root.right.data
                checkBST(root.right)
            else:
                return False
    return True
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
ans=checkBST(root)
print(ans)

'''OUTPUT:
False
'''



