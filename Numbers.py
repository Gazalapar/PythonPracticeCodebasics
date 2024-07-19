#!/usr/bin/env python
# coding: utf-8

# Exercise: Numbers in python
# 1.You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
# 2.You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
# 3.You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
# 4.Print binary representation of number 17

# In[6]:


##1
length=92
width=48.8
area=length*width
print("area of football field:",area)


# In[7]:


##2
packets=9
cost_per_packet=1.49
paid_to_shopkeeper=20
total_cost=packets*cost_per_packet
return_amount=paid_to_shopkeeper-total_cost
print("The shopkeeper give back the money", return_amount)


# In[8]:


##3
length=5.5
cost_per_square=500
area=length**2
total_cost=cost_per_square*area
print("The cost to replace all tiles",total_cost)


# In[9]:


##4
num=17
print('Binary of number 17 is:',format(num,'b'))

