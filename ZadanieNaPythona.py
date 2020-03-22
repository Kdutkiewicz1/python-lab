#!/usr/bin/env python
# coding: utf-8

# In[67]:


from sklearn.datasets import load_boston


# In[68]:


import numpy as np
import pandas as pd


# In[69]:



from sklearn.linear_model import LinearRegression


# In[70]:


boston = load_boston()
boston_data = boston.data
df = pd.DataFrame(data = boston_data, columns = boston.feature_names)
target = 'Price' 
df.insert(13, target , boston.target)
df.head(10)


# In[71]:


column1='INDUS'
column2='NOX'
df.hist(column = column1, bins=150)
df.hist(column = column2, bins=150)


# In[72]:


import matplotlib.pyplot as plt
def linear_regression(x, y, column):
     lin_regression = LinearRegression()
     lin_regression.fit(x, y)
     predict = lin_regression.predict(x)
     plt.scatter(x,y, color = 'yellow')
     plt.plot(x, predict, color= 'blue' )
     plt.xlabel(column)
     plt.ylabel(target)
     plt.show()
linear_regression(df[[column1]], df[[target]], column1)
linear_regression(df[[column2]], df[[target]], column2)


# In[74]:


print('Nitric oxides concentration and  proportion of non-retail business acres per town do not affect the price.\n Unfortunately model is not evenly matched but I dont know how to do it better.')


# In[ ]:




