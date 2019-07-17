#!/usr/bin/env python
# coding: utf-8

# # Data Summary

# This is the summary of sale data, generated in 1000 datas using 3rd party. 
# The datas were in JSON format, consist of "Barang", "Kategori", "harga", "alamat", "Timestamp", "kuantitas", "tanggal lahir", "total harga".
# 
# This part summarize:
# 1. Category of Sales 
# 2. Favourite items (ranked)
# 3. Mean sale per items
# 4. Mean gross sale per items
# 5. Largest gross sale per items (ranked)
# 6. Customer target (age distribution of customers per item)
# 7. Customer's city distribution (ranked)

# In[16]:


import flask
import json
from flask import request, jsonify
import pandas as pd 
import io
import matplotlib.pyplot as plt
import numpy as np
#pd.set_option('display.float_format', lambda x: '%.3f' % x)


# In[17]:


#buat bikin endpoint pake flask, isinya json
app = flask.Flask(__name__)
app.config["DEBUG"] = True

url = 'http://127.0.0.1:5000/api/carsale.json' 
df=pd.read_json(url,orient='columns')
df.to_csv("data.csv")


# In[18]:


# Create some test data for our catalog in the form of a list of dictionaries.
#with open('http://127.0.0.1:5000/api/v1/resources/books/all', 'r') as f:
#    data = json.load(f)

#summary 10 data pertama, tes
df.head(10)


# In[19]:


df.describe()
df.columns


# In[20]:


kategori = df['Kategori'].astype('category')
count_kategori = kategori.value_counts()


# In[21]:


count_kategori = kategori.value_counts()
#count_kategori.plot(kind='hist', x = df["Kategori"], y = count_kategori)


# In[22]:


kategori.value_counts().plot(kind="pie")
plt.title('Jumlah berdasarkan kategori')
plt.legend(labels =kategori.value_counts(),loc='upper left')


# In[23]:


barang = df["Barang"]
count_barang = barang.value_counts()


# In[24]:


#Barang favorit
print("Barang favorit\n")
print(count_barang)


# In[25]:


df.groupby(["Kategori","Barang"]).size().unstack().plot(kind="bar",stacked = True)
plt.title("Jumlah penjualan barang")
plt.legend(loc="upper center",bbox_to_anchor=(1.2, 1))


# In[26]:


x = df["Barang"]
y = df["total harga"]


# In[27]:


print('deskripsi kolom barang')
x.describe()


# In[28]:


print('deskripsi kolom total harga')
y.describe()


# In[29]:


#rata-rata pembelian

df.groupby('Barang').mean()[['kuantitas']]


# In[30]:


#rata-rata laba kotor
print('Laba kotor rata-rata')
df.groupby('Barang', as_index=False)['total harga'].mean()


# In[31]:


#laba kotor maksimum
print('Laba Kotor (descending)')
sumdata = df.groupby('Barang', as_index=False)['total harga'].sum()
sumdata.sort_values(["total harga"], ascending=[0])


# In[32]:


df["tanggal lahir"] = df["tanggal lahir"].astype("datetime64")
tahun_lahir = df["tanggal lahir"].dt.year
count_tahunlahir = (df["tanggal lahir"].dt.year.value_counts ())
tahun_lahir.plot(kind='hist',rwidth =0.8)
plt.title('Distribusi tahun lahir customer')


# In[33]:


#hitung umur pembeli per barang yang dibeli
item = df["Barang"]
age = 2019-tahun_lahir


# In[34]:


#buat dataframe
item_age = pd.DataFrame({'Barang':item, 'Umur':age})


# In[35]:


print('Rata-rata umur untuk setiap barang')
agedata = item_age.groupby('Barang', as_index=False)['Umur'].mean()
agedata.sort_values(["Umur"], ascending=[0])


# In[36]:


item_age["Umur"].plot(kind='hist', bins=[0,12,16,25,35,45,60,70],rwidth = 0.8)


# In[37]:


#item_age.groupby('Barang', as_index=False)['Umur'].plot(kind='hist', bins=[0,12,16,25,35,45,60,70],rwidth = 0.8)
#plt.legend()
#fig_size = plt.rcParams["figure.figsize"]
#fig_size[0] = 9
#fig_size[1] = 7


# In[38]:


item_age.describe()
dat = agedata.sort_values(["Umur"], ascending=[0])
dat["Barang"]


# In[39]:


items = dat["Barang"]
for i in range(len(items)):
    item_age[item_age["Barang"]==items[i]].plot(kind='hist',bins=[0,12,16,25,35,45,60,70],rwidth=0.8)
    plt.title( items[i]+' age distribution')


# In[52]:


kota_count = df["kota"].value_counts()
kota_count.plot(kind='bar')
plt.title('Distribusi kota pembeli')
fig_size = plt.rcParams["figure.figsize"] 
fig_size[0] = 20
fig_size[1] = 10


# In[57]:


#distribusi kota
print('distribusi asal kota pembeli')
df["kota"].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:




