#!/usr/bin/env python
# coding: utf-8

# In[1]:


###stocks analysis####


# In[2]:


##Yahoo Finance	To download stock data
#Pandas	To handle data frames in python
#Numpy	Numerical Python
#Matplotlib	Plotting graphs
### upgrade python pip after importing yfinanace ###


# In[6]:



import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
get_ipython().system('pip install yfinance')
import yfinance as yf
get_ipython().run_line_magic('matplotlib', 'inline')
import datetime
from datetime import timedelta


# In[7]:


### date formats in yyyy-mm-dd with end date less than current day ######


# In[9]:



### num = input("Enter the number of stocks to be analyzed: ") current condition not updated

date_entry = input('Enter the recent stock date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
start_date = str(date1)
default_month = date1 + timedelta(days=-30)
default_year = date1 + timedelta( days=-365)
default_five_year = date1 + timedelta( days=-365 *5)


# In[10]:


start_date


# In[11]:



date_2 = datetime.date(year, month, day)
date_2 = str(default_month)
date_2


# In[12]:



date_3 = datetime.date(year, month, day)
date_3 = str(default_year)
date_3


# In[9]:



date_3 = datetime.date(year, month, day)
date_3 = str(default_five_year)
date_3


# In[10]:


### enter start and end date custom feature ###
##start = "2021-05-17"
##end = '2022-05-16'


# In[11]:


### choose month, date and year functionality #### add month, year and 5 year functionality in if-else code


# In[13]:


t1 = input("Enter the stock 1: ")
t2 = input("Enter the stock 2: ")
t3 = input("Enter the stock 3: ")

end = 'default_month'
fruit =input('enter "month" for recent month analysis \n enter "year" for recent year analysis \n enter "5 year" for 5 year analysis')
if fruit == 'month': 
    end = default_month;

elif fruit == "year": 
    end = default_year;

elif fruit == "5 year": 
    end = default_five_year

else: 
    print("") 


# In[14]:


stock_entry1 = yf.download(t1,end,start_date)
stock_entry2 = yf.download(t2,end,start_date)
stock_entry3 = yf.download(t3,end,start_date)


# In[15]:


stock_entry1


# In[16]:


stock_entry2


# In[17]:


stock_entry3


# In[18]:


stock_entry1['Open'].plot(label = t1, figsize = (15,7))
stock_entry2['Open'].plot(label = t2)
stock_entry3['Open'].plot(label = t3)
plt.title('Enter stocks are = '+str(t1)+" "+str(t2)+" "+str(t3))
plt.legend()


# In[20]:


stock_entry1['High'].plot(label = t1, figsize = (15,7))
stock_entry2['High'].plot(label = t2)
stock_entry3['High'].plot(label = t3)
plt.title('Enter stocks are = '+str(t1)+" "+str(t2)+" "+str(t3))
plt.legend()


# In[19]:


# volume of stock traded ###


# In[21]:


stock_entry1['Volume'].plot(label = t1, figsize = (15,7))
stock_entry2['Volume'].plot(label = t2)
stock_entry3['Volume'].plot(label = t3)
plt.title('Volume of Stock traded')
plt.legend()


# In[23]:


#Market Capitalisation
stock_entry1['MarktCap'] = stock_entry1['Open'] * stock_entry1['Volume']
stock_entry2['MarktCap'] = stock_entry2['Open'] * stock_entry2['Volume']
stock_entry3['MarktCap'] = stock_entry3['Open'] * stock_entry3['Volume']
stock_entry1['MarktCap'].plot(label = t1, figsize = (20,5))
stock_entry2['MarktCap'].plot(label = t2)
stock_entry3['MarktCap'].plot(label = t3)
plt.title('Market Cap')
plt.legend()


# In[22]:


## Rolling the tcs stock with max limit 200 moving avaerage ##


# In[23]:


###Individual weighted average


# In[24]:


tc_code = input("Enter the stock code: ")
if t1 == tc_code: 
    stock_entry1['MA50'] = stock_entry1['Open'].rolling(50).mean()
    stock_entry1['MA200'] = stock_entry1['Open'].rolling(200).mean()
    stock_entry1['Open'].plot(figsize = (15,7))
    stock_entry1['MA50'].plot()
    stock_entry1['MA200'].plot()

elif t2 == tc_code: 
    stock_entry2['MA50'] = stock_entry2['Open'].rolling(50).mean()
    stock_entry2['MA200'] = stock_entry2['Open'].rolling(200).mean()
    stock_entry2['Open'].plot(figsize = (15,7))
    stock_entry2['MA50'].plot()
    stock_entry2['MA200'].plot()

elif t3 == tc_code: 
    stock_entry3['MA50'] = stock_entry3['Open'].rolling(50).mean()
    stock_entry3['MA200'] = stock_entry3['Open'].rolling(200).mean()
    stock_entry3['Open'].plot(figsize = (15,7))
    stock_entry3['MA50'].plot()
    stock_entry3['MA200'].plot()

else: 
    print("") 


# In[25]:


data = pd.concat([stock_entry1['Open'],stock_entry2['Open'], stock_entry3['Open']],axis = 1)
data.columns = [t1, t2, t3]
scatter_matrix(data, figsize = (8,8), hist_kwds= {'bins':250})


# In[26]:



#Volatility
stock_entry1['returns'] = (stock_entry1['Close']/stock_entry1['Close'].shift(1)) -1
stock_entry2['returns'] = (stock_entry2['Close']/stock_entry2['Close'].shift(1)) -1
stock_entry3['returns'] = (stock_entry3['Close']/stock_entry3['Close'].shift(1)) -1
stock_entry1['returns'].hist(bins = 100, label = t1, alpha = 0.5, figsize = (15,7))
stock_entry2['returns'].hist(bins = 100, label = t2, alpha = 0.5)
stock_entry3['returns'].hist(bins = 100, label = t3, alpha = 0.5)
plt.legend()


# In[28]:


stock_entry1['Volume'].plot(label = t1, figsize = (15,7))
stock_entry2['Volume'].plot(label = t2)
stock_entry3['Volume'].plot(label = t3)
plt.title('Enter stocks are = '+str(t1)+" "+str(t2)+" "+str(t3))
plt.legend()


# In[4]:





# In[ ]:




