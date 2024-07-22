#!/usr/bin/env python
# coding: utf-8

# Exercise: Python for loop
# 1.After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
# 
# 2.Print square of all numbers between 1 to 10 except even numbers
# 3.Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.
# 
# 4.Lets say you are running a 5 km race. Write a program that,
# 
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
# 
# 
# 5.Write a program that prints following shape
# 
# *
# **
# ***
# ****
# *****

# In[2]:


"""1.After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads"""
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for item in result:
    if item=="heads":
        count+=1
        
print("The number of times heads occur is", count)    


# In[4]:


#2.Print square of all numbers between 1 to 10 except even numbers
for num in range(1,11):
    if(num%2!=0):
        print(num*num)


# In[2]:


"""3.Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
If expense is not found then it should print that as well."""
month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')


# In[5]:


"""Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message
"""
for run in range(0,5):
    print(f'you run {run+1} miles')
    tired=input("are you tired ?")
    if tired=='yes':
        break
if run==4:
    print(f'you run {run+1} km race ! Woww good job')
else:
    print(f"you didn't finish 5 km race but hey congrats anyways! you still ran {run+1} miles")
        
        
    


# In[18]:


"""5.Write a program that prints following shape

*
**
***
****
*****
"""
for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)

