#!/usr/bin/env python
# coding: utf-8

# Exercise: String in Python
# 1.Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line
# 2.Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index
# 3.Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
# 4.I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

# In[2]:


##1
street="Gorakhnath"
city="Gorakhpur"
country="India"
address=street+"," + city+","+country
print(address)


# In[7]:


address=f'{street},{city},{country}'
print(address)


# In[10]:


##2
string_given="Earth revolves around the sun"
print(string_given[6:14])


# In[15]:


print(string_given[-3:])


# In[25]:


##3
fruits=3
vegies=3
print(f'{"I eat"} {vegies} {"vegies"} {"and"} {fruits} {"fruits daily"}')


# In[26]:


s='maine 200 banana khaye'
s=s.replace('banana','samosa')
s=s.replace('200','10')
print("Using two line replace:",s)

s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)

