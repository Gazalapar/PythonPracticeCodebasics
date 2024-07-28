#!/usr/bin/env python
# coding: utf-8

# Exercise: Python Read Write File
# 1.poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in your python program and find out words with maximum occurance.
# 
# 
# 2.stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
# pe ratio = price / earnings per share
# price to book ratio = price / book value
# Your input format (stocks.csv) is,
# 
# Company Name	Price	Earnings Per Share	Book Value
# Reliance	1467	66	653
# Tata Steel	391	89	572
# Output.csv should look like this,
# 
# Company Name	PE Ratio	PB Ratio
# Reliance	22.23	2.25
# Tata Steel	4.39	0.68

# In[10]:


word_stats={}

with open("C:/Downloads/poem.txt","r") as f:
    for line in f:
      words=line.split(' ')
      for word in words:
        if word in word_stats:
          word_stats[word]+=1
        else:
          word_stats[word] = 1

print(word_stats)

word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)


# In[ ]:




