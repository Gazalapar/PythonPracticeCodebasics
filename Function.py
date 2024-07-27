#!/usr/bin/env python
# coding: utf-8

# Exercise: Functions in python
# 1.Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height
# 2.Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape
# 
# 3.Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
# 
# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

# In[2]:


"""1.Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
Equation of an area of a triangle is,
area = (1/2)*base*height"""

base=input("Enter the base :")
height=input("enter the height :")
base=int(base)
height=int(height)
area=1/2*base*height
print("The area of the triangle is",area)


# In[3]:


"""2.Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape"""



def calculate_area(length,breadth,shape):
    if shape=="triangle":
          area=1/2 *length *breadth
          
    elif shape=="rectangle":
          area=breadth*length
    else:
          area= None
    return area           
    

length=input("Enter the length :")
breadth=input("Enter the breadth :")
shape=input("Enter the shape :")
length=int(length)
breadth=int(breadth)
area=calculate_area(length,breadth,shape)
if area is not None:
    print(f'The area of the {shape} is: {area}')
else:
    print("Invalid shape provided.")


# In[18]:


"""3.Write a function called print_pattern that takes integer number as an argument and 
prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)"""

def print_pattern(num):
    for i in range(num):
        s=""
        for j in range(i+1):
            s=s+'*'
        print(s)           
num=input("Enter the number")
num=int(num)
print_pattern(num)


# In[ ]:




