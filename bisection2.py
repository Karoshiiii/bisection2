#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# get the packages
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


def f(x):
    return (x - x**2)

print(f"f(2) should be - 2; we get {f(2)}")


# In[6]:


# use bisection to find x so f(x) = 0

# try 0.5 for x
print(f" f(0.5) = {f(0.5)}")

#top is x=0.5,
# bot = 2
print(f" f(2) = {f(2)}")


# In[8]:


# bisection algorithm
xHigh = 0.5
xLow = 2

for i in range (10):
    xTry = (xHigh + xLow)/2
    
    if (f(xTry) > 0):
        xHigh = xTry
    else:
        xLow = xTry
        
print(f"final answer = {xTry}, and f = {f(xTry)}")


# In[9]:


print(xLow)
print(xHigh)
x = (xLow+xHigh)/2
print(f(x))


# In[ ]:




