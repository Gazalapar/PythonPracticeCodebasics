#!/usr/bin/env python
# coding: utf-8

# Exercise: Python If Condition
#     
# 1.Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
#   (i)Write a program that asks user to enter a city name and it should tell which country the city belongs to
#   (ii)Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
# 2.Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#  (i)Ask user to enter his fasting sugar level
#  (ii) If it is below 80 to 100 range then print that sugar is low
#   (iii)If it is above 100 then print that it is high otherwise print that it is normal

# In[4]:


india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter city name: ")
if city in india:
    print("The city belongs to India")
if city in pakistan:
    print("The city belongs to pakistan")
if city in bangladesh:
    print("The city belongs to bangladesh")
    


# In[7]:


city1=input("Enter the first city  :")
city2=input("Enter the second city :")
if city1 in india and city2 in india:
    print("Both cities are in india")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("They don't belong to same country")


# In[1]:


"""2.Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
(i)Ask user to enter his fasting sugar level
(ii) If it is below 80 to 100 range then print that sugar is low
 (iii)If it is above 100 then print that it is high otherwise print that it is normal"""
sugar=input("Please enter your fasting sugar level:")
sugar=float(sugar)
if sugar<80:
   print("Your sugar is low, go eat some jalebi :)")
elif sugar>100:
   print("Your sugar is high, stop eating all mithais..!")
else:
   print("Your sugar is normal, relax and enjoy your life!")
   
   


# In[ ]:




