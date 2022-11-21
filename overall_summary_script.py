#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


path=input(r"give path")
df1=pd.read_csv(path) #for city
Unique_column=input("unique_column: ") #for city
Level=input("city/district/village/hex: ")
Table_name=input("Table_name: ")
Remove = input('give column names which want to remove seprated by comma: ').split(",")


# In[ ]:


#make empty datframe with required column names


df2=pd.DataFrame(columns=["Table_name","Level","Indicators","Number_of_rows","No_of_unique_geography_code","Mean","Min","1st_Qu","Median","3rd_Qu","Max","No_of 0","No_of_NA"])
#df2


# In[ ]:


#remove unwanted columns from column_name

column_name=list(df1.columns) 
for i in Remove:
    if i in column_name:
        column_name.remove(i) 
#column_name 



# In[ ]:


#convert all the datacolumns into numeric type

for i in column_name:
    if df1[i].dtype == "object":
        df1[i]=df1[i].str.replace(",","")
        df1[i]=df1[i].astype(float)


# In[ ]:


pd.set_option('display.float_format', lambda x: '%.6f' % x)  #increase decibels


# In[ ]:


df2["Indicators"]=column_name


# In[ ]:


df2["Table_name"]=Table_name
#df2


# In[ ]:


df2["Level"]=Level


# In[ ]:


#count Number_of_rows

Number_of_rows=[]
for i in column_name:
    x=len(df1)
    Number_of_rows.append(x) 
Number_of_rows    

df2["Number_of_rows"]=Number_of_rows


# In[ ]:


#count No_of_unique_geography_code

No_of_unique_geography_code=[]
for i in column_name:
    x=df1[Unique_column].count()
    No_of_unique_geography_code.append(x) 
No_of_unique_geography_code    

df2["No_of_unique_geography_code"]=No_of_unique_geography_code


# In[ ]:


#calculate mean for each indicator
Mean=[]
for i in column_name:
    x=df1[i].mean()
    Mean.append(x) 
Mean    

df2["Mean"]=Mean


# In[ ]:


#calculate minimum value for each indicator

Min=[]
for i in column_name:
    x=df1[i].min()
    Min.append(x) 
Min    

df2["Min"]=Min


# In[ ]:


#calculate first_Qu value for each indicator

first_Qu =[]
for i in column_name:
    x=df1[i].quantile(0.25)
    first_Qu.append(x) 
first_Qu    

df2["1st_Qu"]=first_Qu


# In[ ]:


#calculate Median value for each indicator

Median =[]
for i in column_name:
    x=df1[i].median()
    Median.append(x) 
Median    

df2["Median"]=Median


# In[ ]:


#calculate third_qu value for each indicator

third_qu =[]
for i in column_name:
    x=df1[i].quantile(0.75)
    third_qu.append(x) 
third_qu    

df2["3rd_Qu"]=third_qu


# In[ ]:


#calculate Maximum value for each indicator

Max =[]
for i in column_name:
    x=df1[i].max()
    Max.append(x) 
Max     

df2["Max"]=Max 


# In[ ]:


#calculate No_of_zeros for each indicator


No_of_zeros=[]
for i in column_name:
    x=pd.DataFrame(df1[i])
    zeroes = x[x[i]==0].count()[0]
    No_of_zeros.append(zeroes) 
No_of_zeros     

df2["No_of 0"]=No_of_zeros 


# In[ ]:


#calculate No_of_NA for each indicator

No_of_NA=[]
for i in column_name:
    x=df1[i].isna().sum()
    No_of_NA.append(x) 
No_of_NA     

df2["No_of_NA"]=No_of_NA 


# In[ ]:


#check the samples
df2.iloc[1:40, :]


# In[ ]:


#df1.describe().T


# In[ ]:


#run & save this file only first time
#df2.to_csv(r"C:\sociometric-swapnil\quality_check\overall_summary1.csv",index=False) #to excecute only first time 


# In[ ]:


# append data frame to CSV file       #note-do not execute it 1st time & after that execute it every time
df2.to_csv(r"C:\sociometric-swapnil\quality_check\overall_summary1.csv", mode='a', index=False, header=False)

