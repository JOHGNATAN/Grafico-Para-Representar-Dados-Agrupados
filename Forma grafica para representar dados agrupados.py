#!/usr/bin/env python
# coding: utf-8

#Formatação da figura
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (15, 7))

#Importando base de dados
import pandas as pd
dados = pd.read_csv('C:/Users/JOHGNATAN/OneDrive/Área de Trabalho/Python_Data_Science/base_de_dados_diversos/aluguel_amostra.csv', sep = ';')
dados.head()

# Definindo área do gráfico
area = plt.figure()

g1 = area.add_subplot(1,2,1)
g2 = area.add_subplot(1,2,2)


#Gerando Gráfico >> Dados Agrupados por TIPO
grupo1 = dados.groupby('Tipo').Valor

label = grupo1.count().index
valores = grupo1.count().values

g1.pie(valores, labels = label, autopct = '%1.1f%%', explode = (.1, .1, .1, .1, .1))
g1.set_title('Total de Imóveis por Tipo ')


#Gerando Gráfico >> Dados Agrupados por TIPO AGREGADO
grupo2 = dados.groupby('Tipo Agregado')['Valor']

label1 = grupo2.count().index
valores1 = grupo2.count().values

g2.pie(valores1, labels = label1, autopct = '%1.1f%%', explode = (.1, .2))
g2.set_title('Total de Imóveis por Tipo Agregado')





