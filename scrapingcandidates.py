
# coding: utf-8

# In[1]:


import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[7]:


def countSearch(page):
    
    pattern = {'saúde' : [' saú',' ordem pública ',' pen',' defe',' enferm', 'hospital ',  'médicos'],
               'segurança' : [' segur',' polic',' crim',' violên',' lei',' Milit',' ordem pública',' pen',' defe',' infração','infrator','presidi','preso','vigilân','investig'],
               'educação' : ['educação',' ensino',' professor',' escolas'],
               'economia' : [' economi',' econômi',' produ',' mercado',' indústr',' comérci',' agro',' agric',' serviços',' setor',' terciário',' desenvolv',' terceiriz']}
    candidate = {'saúde' : 0, 'segurança' : 0, 'educação' : 0, 'economia' : 0}
   
    
    page = requests.get(page)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    for key, words in pattern.items():                          
        
        for w in words:     
            
                 candidate[key]+=str(soup.find_all('p')).upper().count(w.upper())
    
    return candidate