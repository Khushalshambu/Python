#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import folium

import re

import geopandas

import matplotlib
import matplotlib.pyplot as plt


# In[2]:


covid_data=pd.read_csv('complete.csv')
covid_data.head()


# In[3]:


India_geoJson = geopandas.read_file('india.json')
India_geoJson.head()


# In[4]:


India_geoJson.plot()


# In[5]:


covid_data['Date']=pd.to_datetime(covid_data['Date']).apply(lambda x: x - pd.DateOffset(days=1))


# In[6]:


covid_data['Death']=pd.to_numeric(covid_data['Death'], errors='coerce')


# In[7]:


covid_data.head()


# In[8]:


covid_data.isnull().sum()


# In[9]:


covid_data = covid_data.dropna(how='any',axis=0)


# In[10]:


covid_data.isnull().sum()


# In[11]:


covid_data['Name of State / UT']=covid_data['Name of State / UT'].apply(lambda x: re.sub('Union Territory of ','',x))
covid_data['Name of State / UT'].replace('Telengana','Telangana',inplace=True)
covid_data['Name of State / UT'].replace('Dadar Nagar Haveli','Dadra and Nagar Haveli',inplace=True)


# In[12]:


id_number={'Andaman and Nicobar Islands': '0',
 'Arunachal Pradesh': '1',
 'Assam': '2',
 'Bihar': '3',
 'Chandigarh': '4',
 'Chhattisgarh': '5',
 'Dadra and Nagar Haveli': '6',
 'Daman and Diu': '7',
 'Goa': '8',
 'Gujarat': '9',
 'Haryana': '10',
 'Himachal Pradesh': '11',
 'Jharkhand': '12',
 'Karnataka': '13',
 'Kerala': '14',
 'Lakshadweep': '15',
 'Madhya Pradesh': '16',
 'Maharashtra': '17',
 'Manipur': '18',
 'Meghalaya': '19',
 'Mizoram': '20',
 'Nagaland': '21',
 'Delhi': '22',
 'Puducherry': '23',
 'Punjab': '24',
 'Rajasthan': '25',
 'Sikkim': '26',
 'Tamil Nadu': '27',
 'Telangana': '28',
 'Tripura': '29',
 'Uttar Pradesh': '30',
 'Uttarakhand': '31',
 'West Bengal': '32',
 'Odisha': '33',
 'Andhra Pradesh': '34',
 'Jammu and Kashmir': '35',
 'Ladakh': '36'}


# In[13]:


covid_data['State_id'] = covid_data['Name of State / UT'].map(id_number)


# In[14]:


covid_data.head()


# In[15]:


covid_data['Active_cases'] = covid_data['Total Confirmed cases']-(covid_data['Cured/Discharged/Migrated']+covid_data['Death'])


# In[16]:


covid_data.isnull().sum()


# In[17]:


covid_data = covid_data.dropna(how='any',axis=0)


# In[18]:


covid_data.isnull().sum()


# In[19]:


bins=np.linspace(min(covid_data['Active_cases']),max(covid_data['Active_cases']),11)
bins


# In[20]:


covid_data['color']=pd.cut(covid_data['Active_cases'],bins,labels=['#FFEBEB','#F8D2D4','#F2B9BE','#EBA1A8','#E58892','#DE6F7C','#D85766','#D13E50','#CB253A','#C50D24'],include_lowest=False)
covid_data['color'].replace(np.nan,'#32CD32',inplace=True)


# In[21]:


covid_data=covid_data[['Date','State_id','color']]


# In[22]:


covid_data.isnull().sum()


# In[23]:


for date in covid_data['Date'].unique():
    diff=set([str(i) for i in range(37)])-set(covid_data[covid_data['Date']==date]['State_id'])
    for i in diff:
         covid_data= pd.concat([covid_data,pd.DataFrame([[date,'#0073CF',i]],columns=['Date','color','State_id'])],ignore_index=True)
covid_data.sort_values('Date',inplace=True)


# In[24]:


covid_data['Date']=(covid_data['Date'].astype(np.int64)// 10**9).astype('U10')
covid_dict={}
for i in covid_data['State_id'].unique():
    covid_dict[i]={}
    for j in covid_data[covid_data['State_id']==i].set_index(['State_id']).values:   
        covid_dict[i][j[0]]={'color':j[1],'opacity':0.7}


# In[25]:


list(covid_dict.items())[10]


# In[26]:


covid_data.dropna(how='any',axis=0)


# In[28]:


India_geoJson['state_id']=India_geoJson['st_nm'].map(id_number)
India_geoJson.drop(columns='st_nm',inplace=True)
India_geoJson.head()


# In[29]:


from folium.plugins import TimeSliderChoropleth


# In[40]:


fig6=plt.Figure(figsize=(1850,2000))
m6 = folium.Map([24, 84], tiles='cartodbpositron', zoom_start=5)
fig6.get_children()


# In[37]:


India_geoJson.drop(columns=['id'])


# In[41]:


g = TimeSliderChoropleth(
    India_geoJson.set_index('state_id').to_json(),
    styledict=covid_dict
).add_to(m6)
m6


# In[ ]:




