#!/usr/bin/env python
# coding: utf-8

# Exercise: Python Variables
# 1.Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.
# 
# 2.Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables
# 
# 3.Store your first, middle and last name in three different variables and then print your full name using these variables
# 
# 4.Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue

# In[1]:


##1
break=5


# This will result in a SyntaxError because break is reserved and cannot be used as a variable name. Here's the error message you would see:
# 
# SyntaxError: invalid syntax
# The reason behind this behavior is that reserved keywords in Python have special meanings and are part of the language's syntax. These keywords cannot be used as identifiers (variable names, function names, etc.) to avoid confusion and to ensure the code remains clear and understandable.

# In[3]:


##2
birth_year=2000
current_year=2024
age=current_year-birth_year
print(age)


# In[5]:


##3
first_name="Gazala"
last_name="parveen"
print(first_name +" "+last_name)


# In[ ]:


##4.Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue
1._nation: Valid. Variable names can start with an underscore.
2.1record: Invalid. Variable names cannot start with a digit.
3.record1: Valid. Variable names can contain digits, as long as they do not start with them.
4.record_one: Valid. Variable names can include underscores.
5.record-one: Invalid. Variable names cannot include hyphens (-).
6.record^one: Invalid. Variable names cannot include caret symbols (^).
7.continue: Invalid. continue is a reserved keyword in Python.
    
So, the invalid variable names are:

1record
record-one
record^one
continue

