#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


df = pd.read_excel("C:/Users/KOUADIO Christiane/Documents/Traitement_données/donnees_sncf.xlsx")


# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[7]:


df['NB_VALD']


# In[8]:


df['NB_VALD'].sort_values()
# ou data.sort_values(by = 'NB_VALD')


# In[9]:


#un dataframe trié sur la serie NB VALD par ordre croissant
df.sort_values(by = 'NB_VALD')


# In[10]:


#tri par ordre décroissant sur la serie NB_VALD
df.sort_values(by = 'NB_VALD', ascending = False)


# In[11]:


#Nouveau dataframe df 1 avec la serie NB_VALD en décroissant
df1=df.sort_values(by = 'NB_VALD', ascending = False)


# In[12]:


df1.head()


# In[13]:


df['NB_VALD']


# In[22]:


df1['NB_VALD'][0:20]


# In[23]:


#Afficher que les 20 premieres lignes 
df1[0:20]


# In[24]:


#Supprimer les doublons dans la serie stations
df1['LIBELLE_ARRET'].drop_duplicates()


# In[25]:


#Nouveau data frame avec les doublons supprimés(les arrêts)
df2=df1.drop_duplicates('LIBELLE_ARRET')


# In[26]:


df2.head()


# In[27]:


df2.shape


# In[32]:


# Question 1) les 20 premières stations en terme de validation 
df2[0:20]
df2['LIBELLE_ARRET'][0:20]


# In[35]:


df3=df2[0:20]
print(df3)


# In[36]:


#Question 2)Illustraton graphique de ce classement
df3.plot.scatter(x='LIBELLE_ARRET', y='NB_VALD')
#Possiblité de faire un mapping pour numéroter les libellés de gares pour un meilleur affichage 
#ou voir les parametres sur l'outil pour un meilleur affichage


# In[37]:


df3['CATEGORIE_TITRE']


# In[110]:


df.groupby(['CATEGORIE_TITRE']).mean()


# In[39]:


#Pour afficher le nombre de valeurs manquantes par serie
df.info()


# In[40]:


#faire le point des valeurs manquantes et ordonner par ordre décroissant
df.isnull().sum().sort_values(ascending=False)


# In[41]:


# (include='0') pour avoir aussi les statistiques sur les variables catégoriques
#data.describe(include='0')
df.describe()


# In[42]:


#)
df.dtypes


# In[43]:


#Renseinger les valeurs manquantes en séparants le fichiers en deux( les valeurs numériques et les chaines de caractères)
cat_df=[]
num_df=[]
for i,c in enumerate(df.dtypes):
    if c==object:
        cat_df.append(df.iloc[:,i])
    else:
            num_df.append(df.iloc[:,i])
cat_df


# In[50]:


df.groupby(['LIBELLE_ARRET','NB_VALD']).mean()


# In[51]:


df.groupby(['LIBELLE_ARRET','NB_VALD']).mean()[0:20]


# In[53]:


# total de nombre de validation par arrêts
df.groupby(['LIBELLE_ARRET']).sum()


# In[67]:


#le tableau précédents va constituer mon dataframe de base dans lequel je vais ordonner par ordre décroissant le 
#nombre de validation pour avoir la première station en terme de classement en fonction de NBRE DE VALIDATION
dfA=df.groupby(['LIBELLE_ARRET']).sum()
dfAO=dfA.sort_values(by = 'NB_VALD', ascending = False)


# In[55]:


dfAO[0:20]


# In[93]:


dfAO1=dfAO.drop(columns=['CODE_STIF_TRNS','ID_REFA_LDA'])[0:20]


# In[94]:


# Les 20 premières stations en terme de nombre de validation
print(dfAO1)


# In[95]:


#Question 2)Illustraton graphique de ce classement
#dfAO1.plot.scatter(x='LIBELLE_ARRET', y='NB_VALD')
dfAO2=df.drop(columns=['JOUR','CODE_STIF_RES','CODE_STIF_TRNS','ID_REFA_LDA','CODE_STIF_ARRET','CATEGORIE_TITRE'])


# In[96]:


print(dfAO2)


# In[98]:


dfAO2.groupby(['LIBELLE_ARRET','NB_VALD']).sum()


# In[106]:


dfAO2.groupby(['LIBELLE_ARRET']).sum()


# In[107]:


dfAO3=dfAO2.groupby(['LIBELLE_ARRET']).sum()
dfAO4=dfAO3.sort_values(by = 'NB_VALD', ascending = False)


# In[108]:


dfAO4[0:20]


# In[109]:


dfAO4.plot.scatter(x='LIBELLE_ARRET', y='NB_VALD')


# In[ ]:




