#!/usr/bin/env python
# coding: utf-8

# Exercise: Python Dict and Tuples
# 1.We have following information on countries and their population (population is in crores),
# 
# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format,
# china==>143
# india==>136
# usa==>32
# pakistan==>21
# add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
# query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
# 
# 
# 2.You are given following list of stocks and their prices in last 3 days,
# 
# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]
# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.
# 
# 
# 3.Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

# In[15]:


"""1.We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	32
Pakistan	21
Using above create a dictionary of countries and its population
Write a program that asks user for three type of inputs,
print: if user enter print then it should print all countries with their population in this format,
china==>143
india==>136
usa==>32
pakistan==>21
add: if user input add then it should further ask for a country name to add. 
If country already exist in our dataset then it should print that it exist and do nothing.
If it doesn't then it asks for population and add that new country/population in our dictionary and print it
remove: 
when user inputs remove it should ask for a country to remove. 
If country exist in our dictionary then remove it and print new dictionary using format shown above in (a).
Else print that country doesn't exist!
query: on this again ask user for which country he or she wants to query.
When user inputs that country it will print population of that country.
"""

def printAll():
    print("The data is as follows :")
    for key,value in population.items():
        
        print(f'{key}==>{value}')
def add_data():
     
        country_name=input("Enter the country you want to add :")
        country_name=country_name.lower()
    
        if country_name in population:
            print("Already present:) ") 
            return
        
        popl=input(f'enter the population for {country_name} : ')
        popl=float(popl)
        population[country_name]=popl
        printAll()
def remove_data():
    
    country=input("Enter the country you want to remove :")
    country=country.lower()
    if country not in population:
        print("Country does not exist!")
        return
    del population[country]
    printAll()
def query():
    query=input("enter the country you want query for : ")
    query=query.lower()
    if query in population:
        print(f'The population for the {query} is {population[query]}')
        return
    print("The country does not exit!")
        
        
    
        
    
            
        
       
    
    

population = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21
}
operation=input("Enter the operation you want to perform :")
operation=operation.lower()
if operation=="print":
    printAll()
elif operation=="add":
    add_data()
elif operation=="remove":
    remove_data()
elif operation=="query":
    query()
else:
    print("Invalid operation!! try again.....")
    


# In[7]:


"""2.You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', 
it asks for stock ticker and price.
If stock already exist in your list (like info, ril etc) then it will append the price to the list.
Otherwise it will create new entry in your dictionary.
For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks."""
import statistics
stock={"info":[600,630,620],
       "ril":[1430,1490,1567],
       "mtl":[234,180,160]
      }
def print_all():
    print("The Data is as follows :")
    for key ,value in stock.items():
        avg=statistics.mean(value)
        print(f'{key} ==>{value} ==> avg: {round(avg,2)} ')
def add():
    s = input("Enter a stock ticker to add:")
    p = input("Enter price of this stock:")
    p=float(p)
    if s in stock:
        stock[s].append(p)
    else:
        stock[s] = [p]
    print_all()
     
def main():
    op=input("Enter operation (print, add or amend):")
    if op.lower() == 'print':
        print_all()
    elif op.lower() == 'add':
        add()
    else:
        print("Unsupported operation:",op)

if __name__ == '__main__':
    main()


# In[10]:


"""3.Write circle_calc() function that takes radius of a circle as an input from user and 
then it calculates and returns area, circumference and diameter.
You should get these values in your main program by calling circle_calc function and then print them"""
import math
def circle_calc(radius):
    area=math.pi*(radius**2)
    circumference=2*math.pi*radius
    diameter=2*radius
    return area , circumference ,diameter 
if __name__=="__main__":
    radius=input("enter the radius of the circle :")
    radius=float(radius)
    a ,c ,d=circle_calc(radius)
    print(f'The area is {round(a,2)}. The circumference is {round(c,2)}. The diameter is {round(d,2)}  ')
    

