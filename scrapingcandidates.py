
# coding: utf-8

import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


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


# ## Paulo Rabello de Castro (PSC)

# In[5]:


#trocar esse site pois não mostra as propostas do candidato
#countSearch("https://www1.folha.uol.com.br/poder/2018/03/filiado-ao-psc-rabello-de-castro-deixa-bndes-para-disputar-eleicoes.shtml")
countSearch("http://congressoemfoco.uol.com.br/eleicoes-2014/programa-de-governo-de-levy-fidelix/")


# ## Michel Temer (MDB)
# 

# In[19]:


#trocar esse site pois não mostra as propostas do candidato
countSearch("http://micheltemer.com.br/frases/")


# ## Henrique Meirelles (PSD)

# In[20]:


#trocar esse site pois não mostra as propostas do candidato
countSearch("http://investimentosenoticias.com.br/eleicoes/henrique-meirelles-candidato-a-presidencia-em-2018")


# ## Aldo Rebelo e Beto Albuquerque (PSB)

# In[21]:


#trocar esse site pois não mostra as propostas do candidato

countSearch("https://exame.abril.com.br/brasil/solidariedade-lanca-aldo-rebelo-como-pre-candidato-a-presidente/")


# ## Valéria Monteiro (PMN)

# In[22]:



countSearch("https://veja.abril.com.br/blog/veja-gente/valeria-monteiro-candidata-a-presidente-sou-uma-via-de-reacao/")


# In[23]:


#trocar esse site pois não mostra as propostas do candidato
countSearch("https://noticias.uol.com.br/politica/eleicoes/2018/noticias/2018/03/05/pre-candidata-ex-jornalista-da-globo-estuda-usar-bordao-no-estilo-eneas.htm")


# ## Rodrigo Maia (DEM)

# In[24]:


#trocar esse site pois não mostra as propostas do candidato
countSearch("http://www.gazetadopovo.com.br/eleicoes/2018/dem-lanca-maia-para-presidente-e-divulga-proposta-liberal-humanista-414ifo7ajuye81q47t1ay9s41")


# ## Marina Silva (Rede)

# In[25]:


countSearch("http://marinasilva.org.br/programa/#pagina-107")


# ## Manuela D'Ávila (PC do B)

# In[26]:


#trocar esse site pois não mostra as propostas do candidato
countSearch("http://bardebatom.com.br/noticia/manuela-davila-conheca-a-candidata-a-presidencia")


# In[27]:


#trocar esse site pois não mostra as propostas do candidato
countSearch("http://www.redebrasilatual.com.br/politica/2017/11/pre-candidata-manuela-davila-defende-consulta-para-revogar-medidas-de-temer")

