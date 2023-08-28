#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


cric =pd.read_csv(r"C:\Users\Swarup\OneDrive - D Y Patil Education Society\Desktop\test.csv") 


# In[3]:


cric


# In[5]:


cric.isna().sum()


# In[14]:


df=cric.iloc[:,:-1]


# In[15]:


df


# In[16]:


df.isna().sum()


# In[17]:


df.head()


# In[18]:


df.tail()


# In[19]:


df.sample(5)


# In[28]:


df.isin(['-']).sum()


# In[29]:


df=df.replace('-',0)


# In[31]:


df.tail()


# In[42]:


player=df.iloc[:,1:2]
player=np.array(player)
player


# In[61]:


p_name=[]
country=[]
for i in range(3000):
    for i in player[i]:
        pi.split("("))
        p_name=


# In[70]:


p_name=[]
country=[]
for j in range(3000):
    for i in player[j]:    
        split_values = i.split('(')
        q_name = split_values[0].strip()
        
        coun1 = split_values[1].replace(')', '').strip()


        #print("Player Name:", q_name)
        #print("Nation:", coun1)
        p_name.append(q_name)
        country.append(coun1)


# In[73]:


p_name


# In[72]:


country


# In[97]:


d={'plyerName':p_name,'Country':country}


# In[99]:


x=pd.DataFrame(d)


# In[100]:


x


# In[101]:


y=df.iloc[:,2:]


# In[102]:


y


# In[107]:


cricket=pd.concat([x,y],axis=1)


# In[108]:


cricket


# In[109]:


cricket=cricket.iloc[:-1]


# In[110]:


cricket


# In[111]:


cricket.to_csv("cricket1",index=False)


# In[1]:


player=cricket.iloc[:,1:2]
player=np.array(player)
player


# In[ ]:




