#!/usr/bin/env python
# coding: utf-8

# In[5]:


# modules we'll use
import pandas as pd
import numpy as np
# read in all our data
df = pd.read_csv (r'C:\Users\user\Downloads\archive\Building_Permits.csv')
print (df)
 # set seed for reproducibility
np.random.seed(0)


# In[7]:


# look at a few rows of the nfl_data file. I can see a handful of missing data already!
df.sample(5)


# In[8]:


# get the number of missing data points per column
missing_values_count = df.isnull().sum()

# look at the # of missing points in the first ten columns
missing_values_count[0:10]


# In[9]:


total_cells = np.product(df.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
(total_missing/total_cells) * 100


# In[10]:


# your turn! Find out what percent of the sf_permits dataset is missing
total_cells = np.product(df.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
(total_missing/total_cells) * 100


# In[11]:


# look at the # of missing points in the first ten columns
missing_values_count[0:10]


# In[12]:


# remove all the rows that contain a missing value
df.dropna()


# In[13]:


# remove all columns with at least one missing value
columns_with_na_dropped = df.dropna(axis=1)
columns_with_na_dropped.head()


# In[14]:


# just how much data did we lose?
print("Columns in original dataset: %d \n" % df.shape[1])
print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])


# In[15]:


# Your turn! Try removing all the rows from the sf_permits dataset that contain missing values. How many are left?
rows_with_na_dropped = df.dropna(axis=1)
rows_with_na_dropped.head()


# In[17]:


# Now try removing all the columns with empty values. Now how much of your data is left?

columns_with_na_dropped = df.dropna(axis=1)
columns_with_na_dropped.head()

print("Columns in original dataset: %d \n" % df.shape[1])
print("Columns with na's dropped: %d" % df.shape[1])


# In[ ]:




