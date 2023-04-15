#!/usr/bin/env python
# coding: utf-8

# In[41]:


#importing the modules
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
#from sklearn import metrics


# In[43]:


#reading the data set
data = pd.read_csv('London hotel prices.csv')
print(data)


# In[34]:


X = data.iloc[:, :-1]
y= data.iloc[:, -1]


# In[35]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=1)


# In[36]:


print(X_train)


# In[37]:


print(y_train)


# In[ ]:




