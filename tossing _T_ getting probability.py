#!/usr/bin/env python
# coding: utf-8

# In[17]:


import random as rd

coin = ["H", "T"]
count = 0

with open("data.csv", "w") as f:
    f.write("Iteration,Flip,Total_Tails,Ratio\n")  # write header

for i in range(1, 100001):
    k = rd.choice(coin)
    if k == "T":
        count += 1
    with open("data.csv", "a") as f:
        f.write(f"{i},{k},{count},{count/i:.4f}\n")


# In[18]:


import pandas as pd


# In[19]:


df=pd.read_csv("data.csv")


# In[20]:


df


# In[21]:


get_ipython().system('pip install matplotlib')


# In[22]:


import matplotlib.pyplot as plt
plt.plot(df['Iteration'],df['Ratio'])
plt.grid(True)
plt.axhline(y=0.5, color='red', linestyle='--')
plt.show()


# In[ ]:




