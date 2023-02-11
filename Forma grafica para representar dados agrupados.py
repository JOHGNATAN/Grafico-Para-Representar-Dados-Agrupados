#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15, 7))


# In[4]:


import pandas as pd
dados = pd.read_csv('C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/aluguel_amostra.csv', sep = ';')
dados.head()


# In[16]:


area = plt.figure()

g1 = area.add_subplot(1,2,1)
g2 = area.add_subplot(1,2,2)

grupo1 = dados.groupby('Tipo').Valor
label = grupo1.count().index
valores = grupo1.count().values
g1.pie(valores, labels = label, autopct = '%1.1f%%', explode = (.1, .1, .1, .1, .1))

grupo2 = dados.groupby('Tipo Agregado')['Valor']
label1 = grupo2.count().index
valores1 = grupo2.count().values
g2.pie(valores1, labels = label1, autopct = '%1.1f%%', explode = (.1, .2))


# In[ ]:




