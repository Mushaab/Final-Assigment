#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# Load first dataset
df1 = pd.read_csv('business.retailsales.csv')

# Load second dataset
df2 = pd.read_csv('business.retailsales2.csv')
df1.head()
df1.describe()
df2.head()
df2.describe()


# In[2]:


df1 = df1.dropna()
df2 = df2.dropna()


# In[3]:


# Rename columns for data1
df1.columns = ['ProductType', 'NetQuantity', 'GrossSales', 'Discounts', 'Returns', 'TotalNetSales']

# Rename columns for data2
df2.columns = ['Month', 'Year', 'TotalOrders', 'GrossSales', 'Discounts', 'Returns', 'NetSales', 'Shipping', 'TotalSales']


# In[4]:


df1.head()


# In[5]:


df2.head()


# In[20]:


new_data = pd.merge(df1, df2, on='Returns')
print("New Merged Dataset:\n", new_data)


# In[22]:


new_data.head()



# In[ ]:




