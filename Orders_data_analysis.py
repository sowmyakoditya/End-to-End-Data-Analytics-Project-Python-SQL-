#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Reading CSV File

import pandas as pd
df = pd.read_csv('orders.csv')


# In[4]:


df


# In[7]:


#Handling Null Values
df['Ship Mode'].unique()


# In[10]:


# Now I want to treat 'Not Available', 'unknown' as nan

df = pd.read_csv('orders.csv', na_values=['Not Available','unknown'])


# In[11]:


df['Ship Mode'].unique()


# In[16]:


#rename columns names ..make them lower case and replace space with underscore

#df.rename(columns={'Order Id':'order_id', 'City':'city'})
#df.columns=df.columns.str.lower()
#df.columns=df.columns.str.replace(' ','_')
df.head(5)


# In[20]:


#derive new columns discount , sale price and profit

#df['discount']=df['list_price']*df['discount_percent']*.01
#df['sale_price']= df['list_price']-df['discount']
#df['profit']=df['sale_price']-df['cost_price']
df


# In[22]:


#convert order date from object data type to datetime

df.dtypes


# In[23]:


#convert order date from object data type to datetime

df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[24]:


df.dtypes


# In[25]:


#drop cost price list price and discount percent columns


df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True)


# df

# In[29]:


#Connecting to SSMS
import sqlalchemy as sal
engine = sal.create_engine('mssql://ShravanSowmya/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[30]:


#load the data into sql server using replace option

df.to_sql('df_orders', con=conn , index=False, if_exists = 'replace')


# ### If we use "replace option" pandas will create a table with highest possible datatypes like varchar(max), bigint. So create a table in SSMS and use "append option" to load the data to df_orders

# In[33]:


#load the data into sql server using append option

df.to_sql('df_orders', con=conn , index=False, if_exists = 'append')

