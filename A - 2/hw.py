# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 09:25:36 2020

@author: G.S Ramchandra
"""



import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

adf = pd.read_csv("C:/Users/G.S Ramchandra/Desktop/Varchala/GSU/Classes/FDS/A - 2/auto-mpg.csv")
adf.head()

#%%


#%%
# Answer to Q1
desc = pd.DataFrame(columns=['Data Type','Data Scale'])
desc['Data Type'] = adf[adf.columns].dtypes
desc.loc[desc['Data Type'] == object, 'Data Type'] = 'categorical'
# desc.loc[desc['Data Type'] != 'categorical', 'Data Type'] = 'numerical'
desc.loc[desc['Data Type'] != 'categorical', 'Data Scale'] = 'Ratio'
desc.loc[desc['Data Type'] == 'categorical', 'Data Scale'] = 'Nominal'
desc.head(9)

#%%
# Your answer to Q2 goes here!
print(adf.nunique())
print(adf.isnull().sum())


#%%
# For categorical attributes
fig, ax = plt.subplots(2,2,squeeze=False,constrained_layout=True,figsize=(5,5))
# fig.figsize=(10,3)
ax[0][0].bar(adf['origin'].unique(),adf['origin'].value_counts())
ax[0][0].set_title('origin')

ax[0][1].bar(adf['year'].unique(),adf['year'].value_counts())
ax[0][1].set_title('year')

ax[1][0].bar(adf['cylinders'].unique(),adf['cylinders'].value_counts())
ax[1][0].set_title('cylinders')

ax[1][1].set_visible(False)


plt.show()


#%%

# For numerical attributes
fig, ax = plt.subplots(3,2,squeeze=False,constrained_layout=True,figsize=(6,6))
# fig.figsize=(10,3)
ax[0][0].hist(adf['mpg'], bins=10)
ax[0][0].set_title('mpg')

ax[0][1].hist(adf['displacement'], bins = 30)
ax[0][1].set_title('displacement')

ax[1][0].hist(adf['horsepower'],)
ax[1][0].set_title('horsepower')

ax[1][1].hist(adf['acceleration'])
ax[1][1].set_title('acceleration')

ax[2][0].hist(adf['weight'],bins=10)
ax[2][0].set_title('weight')

ax[2][1].set_visible(False)


plt.show()


#%%

# Answer to Q4 goes here
# print(adf.describe())
print(adf.describe())
print("Skew is :--------", adf.skew())
def outlier_detection (col):
#     print(col.describe())
    median = col.median()
    std = col.std()
    min_range = median - 2*std
    max_range = median + 2*std
    #print (col[(col > max_range) | (col < min_range)])
    #print ( (col[col < max_range]).max())
    col.loc[col > max_range] = (col[col < max_range]).max()
    col.loc[col < min_range] = (col[col > min_range]).min()
#     print(col.describe())
    return col
    
# print(adf.skew())

adf.loc['mpg'] = outlier_detection(adf['mpg'])
adf.loc['displacement'] = outlier_detection(adf['displacement'])
adf.loc['horsepower'] = outlier_detection(adf['horsepower'])
adf.loc['acceleration'] = outlier_detection(adf['acceleration'])
adf.loc['weight'] = outlier_detection(adf['weight'])

print(adf.describe())

print("Skew is :--------", adf.skew())



#%%


# For numerical attributes
fig, ax = plt.subplots(3,2,squeeze=False,constrained_layout=True,figsize=(6,6))
# fig.figsize=(10,3)
ax[0][0].hist(adf['mpg'], bins=10)
ax[0][0].set_title('mpg')

ax[0][1].hist(adf['displacement'], bins=30)
ax[0][1].set_title('displacement')

ax[1][0].hist(adf['horsepower'],bins=10)
ax[1][0].set_title('horsepower')

ax[1][1].hist(adf['acceleration'])
ax[1][1].set_title('acceleration')

ax[2][0].hist(adf['weight'],bins=10)
ax[2][0].set_title('weight')

ax[2][1].set_visible(False)


plt.show()


#%%

# dqr_cont = np.array([['Feature','Count','% Miss','Cardinality','Min','1st Q','Mean','Median','3rd Q','Max', 'S.D.']])
# dqr_cat = np.array([['Count','% Miss','Cardinality','Mode','Mode freq','Mode %','2nd Mode','2nd Mode freq','2nd Mode %']])

class DQR():
 def __init__(self):
        self.dqr_cont = pd.DataFrame(columns=['Feature','Count','% Miss','Cardinality','Min','1st Q','Mean','Median','3rd Q','Max', 'S.D.'])
        self.dqr_cat = pd.DataFrame(columns=['Feature','Count','% Miss','Cardinality','Mode','Mode freq','Mode %','2nd Mode','2nd Mode freq','2nd Mode %'])
        self.dqr_cont['Feature'] = ['mpg','displacement','horsepower','weight','acceleration']
        self.dqr_cat['Feature'] = ['year','cylinders','origin','carname']
 
 def report(self, data):
        data = pd.DataFrame(data)
        for col in data.columns:
            if(col == 'year' or col == 'origin' or col == 'carname' or col == 'cylinders'):
                mode = data[col].value_counts().index
                mode_freq = data[col].value_counts().values
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'Count'] = data[col].count()
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'Cardinality'] = data[col].nunique()
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'Mode'] = mode[0]
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'Mode freq'] =  mode_freq[0]
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'Mode %'] = (mode_freq[0] / (data[col].count()))*100
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'2nd Mode'] = mode[1]
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'2nd Mode freq'] = mode_freq[1]
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'2nd Mode %'] = (mode_freq[1] / (data[col].count()))*100
                self.dqr_cat.loc[self.dqr_cat['Feature'] == col,'% Miss'] = ((data[col].isnull().sum())/ (data[col].count()))*100

            else:
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'Count'] = data[col].count()
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'% Miss'] = ((data[col].isnull().sum())/ (data[col].count()))*100
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'Cardinality'] = data[col].nunique()
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'Min'] = data[col].min()
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'1st Q'] = data[col].quantile(0.25)
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'Mean'] = data[col].mean()
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'Median'] = data[col].median()
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'3rd Q'] = data[col].quantile(0.75)
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'Max'] = data[col].max()
                self.dqr_cont.loc[self.dqr_cont['Feature'] == col,'S.D.'] = data[col].std()


obj3 = DQR()
# print(adf.copy())
obj3.report(adf.copy())
# print("Data Quality report for Catgorical variable: ")
# print(dqr_cat)
# print("Data Quality report for Continuous variable: ")
print(obj3.dqr_cont)

obj3.dqr_cat.head()


