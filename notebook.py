#!/usr/bin/env python
# coding: utf-8

# In[2]:


# imports and whatnot
# get the data
import requests
import urllib.parse
import zipfile
import os


# In[4]:


# Download the data file
# - URL Query string
scheme = 'https'
host = 'data.cms.gov'
fileName = '/data-api/v1/dataset/128d9a55-49d9-4be7-b33b-ce236bebdeca/data-viewer'
query = {
    '_format': 'csv'
}
# Send request
r = requests.get(
    f'{scheme}://{host}/{fileName}?{urllib.parse.urlencode(query)}',
    allow_redirects=True
)

zipFileName = './web/data-download.zip'
os.makedirs(os.path.dirname(zipFileName), exist_ok=True)

# Download file
with open(zipFileName, 'wb') as f:
    f.write(r.content)

#unzip file into working directory
with zipfile.ZipFile(zipFileName, 'r') as z:
    z.extractall('.')


# In[ ]:


# Verify we can read dataset

