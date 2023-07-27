#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Business Problem - 


# In[1]:


#import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#load the data
data = pd.read_excel(r"C:\Users\Aditi nath\Downloads\EDA\Jupyter data.xlsx")


# In[3]:


data


# In[4]:


#get information about the data
data.info() #no null values


# In[5]:


#Get statistical information
data.describe() #outlier detected in both diamond weight and price 


# In[6]:


#drop unneccesary column
data = data.drop('id',1)


# In[7]:


data.corr() #Weight and price high correlation  but what about shape and cut because uska bhi directly impact padhta hai price mai 


# In[8]:


data.isnull().sum() #Doubt info m null value nhi rtha but isnull lagane se pata chl raha


# In[9]:


#Get occurence of each categorical data 
data['diamond_shape'].value_counts()


# In[10]:


data['diamond_cut_grade'].value_counts()


# In[11]:


data['diamond_color'].value_counts()


# In[12]:


data['diamond_clarity'].value_counts()


# In[13]:


#Remove null value from dataset because its very few
data = data.dropna()
data


# In[14]:


#data visualization
plt.figure(figsize=(8, 6))
plt.hist(data['diamond_shape'],bins=20) #How can we define bin is there any method ?
plt.show()


# In[15]:


plt.figure(figsize=(8, 6))
plt.hist(data['diamond_weight'],bins=20) #how ?
plt.show() #Can we take 3 carat diamond weight beacuse according to the visualization maximum weight upto 0 -3 


# In[16]:


plt.figure(figsize=(8, 6))
plt.hist(data['price'],bins=20)   #maximum price show in statistical summary is 116869 but in graph upto 25k shown
plt.show()


# In[17]:


#heatmap
#How diamond weight effecting the price?
plt.figure(figsize=(5,5))
sns.heatmap(data.corr(),cbar = True,annot=True,cmap='Blues')


# #Diamond Weight is positive correaltion to the price 

# In[18]:


#Relationship between diamond_shape and price with box plot
sns.boxplot(x ='price',y ='diamond_shape',data=data)


# In[19]:


sns.boxplot(x='price',y='diamond_color',data=data) #problem facing in analyses because of outliers


# In[10]:


import plotly.express as ps
fig = ps.box(data,y=['diamond_weight'])
fig.show()


# In[11]:


fig = ps.box(data,y=['price'])
fig.show()


# In[20]:


#Refrence - https://www.analyticsvidhya.com/blog/2021/08/how-to-perform-exploratory-data-analysis-a-guide-for-beginners/


# In[21]:


#Questions
#1) #Weight and price high correlation  but what about shape and cut because uska bhi price mai directly impact padhta hai
#2)#Doubt info m null value nhi rtha but isnull lagane se pata chl raha
#3) #Can we take 3 carat diamond weight beacuse according to the visualization maximum weight upto 0 -3  -- (In input 15)
#4) #How can we define bin is there any method ? --(Input 14)
#5) #maximum price show in statistical summary is 116869 but in graph upto 25k shown--(Question related to describe and graph differnce[[input 16]])
#6)  #problem facing in analyses because of outliers --(input- 19)

