#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


pd.set_option('display.max_columns', None)


# In[3]:


df=pd.read_csv('soccer.csv')
df.head()


# In[4]:


df.shape


# In[5]:


print('NO OF ROWS:',df.shape[0])
print('NO OF COLUMNS :', df.shape[1])


# # Q1: What is the total number of goals scored in the entire dataset?
# 
# 
# 

# In[6]:


df['Goals'].unique()


# In[7]:


df['Goals'].sum()


# # Q2: Which player has scored the most goals as a substitution

# In[8]:


df[['Goals','Substitution ']].sort_values(by='Substitution ',ascending=False)


# In[9]:


df[['Goals','Substitution ','Player Names']].sort_values(by='Substitution ',ascending=False).head(1)


# # Q3: Find the top 5 players with the most number of goals scored. Also find the total number of goals scored by them

# In[10]:


df[['Goals','Player Names']].sort_values(by='Goals',ascending=False).head(5)


# In[11]:


df['Goals'].sort_values(ascending=False).head(5).sum()


# # Q4: What are the top 10 countries with the most number of players in the dataset?

# In[12]:


df['Country'].unique()


# In[13]:


df[['Country','Player Names']].value_counts()


# # Q5: # Q1. Create a new dataframe after removing the ourliers for Mins Column in the dataset (conside the upper quantile to be 99 percentile and the lower quantile to be 1 percentile.). After that Find the difference in the number of rows?
# 
# * Difference is df.shape(only rows) - df.shape(rows of filtered data only)

# In[14]:


sns.distplot(df['Mins'])
plt.show()


# In[15]:


df.describe()


# In[16]:


min_limit=df['Mins'].quantile(0.01)
max_limit=df['Mins'].quantile(0.99)


# In[17]:


min_limit


# In[18]:


max_limit


# In[19]:


df[(df['Mins']>max_limit) | (df['Mins']<min_limit)]


# In[20]:


len(df[(df['Mins']>max_limit) | (df['Mins']<min_limit)])


# In[21]:


df_new=df[(df['Mins']<max_limit) & (df['Mins']>min_limit)]
df_new


# In[22]:


sns.boxplot(df_new['Mins'])


# # Q7. Using Bar Plot show in which year has Cristiano Ronaldo scored the most number of goals?

# In[23]:


df_new_data=df[df['Player Names']=='Cristiano Ronaldo'][['Year','Goals']].max()


# In[24]:


df_new_data


# # Q8. In the year 2019 who has more Goals between Ronaldo and Messi? 
# - First print them normally 
# - Display the comparison using a bar plot

# In[25]:


df[df['Year']==2019][['Player Names','Goals']].sort_values(by='Goals',ascending=False)


# In[26]:


df_new1=df[(df['Player Names']=='Cristiano Ronaldo') | (df['Player Names']=='Lionel Messi')]


# In[27]:


data_new=df_new1[df_new1['Year']==2019][['Player Names','Goals']]
data_new


# In[28]:


data_new.plot(kind='bar')


# # Q9: Using Pie Chart show the amount of data various Countries are containing in this dataset(use the Country Columns Display the percentage of data as well in the pie chart

# In[29]:


df.head(1)


# In[30]:


df.groupby('Country').size().plot(kind = 'pie', autopct = '%.1f', figsize = (6,6))


# # Q10: Display a Heatmap  to show the correlation between the columns in the dataset. The heatmap should have the value of the correlation printed within the boxes.

# In[31]:


df.corr()


# In[32]:


sns.heatmap(df.corr())


# # Q11: Which Country has the maximum median OnTarget Shots among all the Countries in the year 2020?

# In[33]:


df.head(1)


# In[34]:


df['ONTargetShots']=df['OnTarget']/df['Shots']*100


# In[52]:


df.head(1)


# In[54]:


df['ONTargetShots'].median()


# In[62]:


df[df['ONTargetShots']>44.0][['Country','ONTargetShots']].sort_values(by='ONTargetShots',ascending=False)


# In[63]:


df[df['ONTargetShots']>44.0][['Country','ONTargetShots']].sort_values(by='ONTargetShots',ascending=False).head(1)


# # Q12. Who has the best average  Goals per minute?
# * Consider only those players who have played more than 30 games
# * Then Find Goals per minute
# * Find Mean of Goals per minute and sort the values

# In[37]:


df_new_1=df[df['Matches_Played']>30]


# In[38]:


df_new_1['Goals_Per_Minute']=df_new_1['Goals']/df_new_1['Mins']


# In[39]:


df_new_1.mean().sort_values(ascending=False)


# # Q 13. Which Player has the least and most number of missed shots in the dataset?
# * Missed Shots=Shots-On Target

# In[40]:


df['Missed Shots']=df['Shots']-df['OnTarget']


# In[41]:


df.groupby(by='Missed Shots')['Player Names'].min()


# # Q14: How many countries have had players who played more than 35 matches? Create a bar plot to display the count for each country.

# In[44]:


data_new=df[df['Matches_Played']>35]
len(data_new['Country'])


# # Q15: Draw a Line Chart to show the comparison of the top 5 highest scoring players in the dataset throughout the years(2016-2020)
# 

# In[47]:


df.head(1)


# In[85]:


for i in df['Year']:
    if( i>=2016 and i <=2020):
           print(i)


# In[ ]:





# In[ ]:




