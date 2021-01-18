#!/usr/bin/env python
# coding: utf-8

# # Plot somme basis plots with `python` and `matplot` library

# In[1]:


get_ipython().run_line_magic('cat', '/ifb/data/mydatalocal/stat-merged.csv')


# #### Put the correct file name of your csv file generated previously with the python script 

# In[2]:


csv_file="/ifb/data/mydatalocal/stat-merged.csv"

# Load the csv file into a python/panda dataframe
df1 = pd.read_csv(csv_file, index_col=False)


# #### Plot the reads number by fastq file 

# In[64]:


# Define the size of the figure
plt.figure(figsize=(20, 5))
ax = plt.gca()

df1.plot(x='sample', y='reads',kind="bar", color='blue', ax=ax, linewidth=3)
plt.title('PUT YOUR TITLE', fontsize=10)
plt.xlabel('PUT X LABEL')
plt.ylabel('PUT Y LABEL')
plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='8',
    )

plt.show()


# #### Plot the length mean 

# In[69]:


# Define the size of the figure
plt.figure(figsize=(8, 5))
ax = plt.gca()

#dot plot of the mean length by file
df1.plot(x='sample', y='len',kind="scatter", color='blue', ax=ax, linewidth=3)
df1.plot(x='sample', y='len_mean',kind="scatter", color='forestgreen', ax=ax, linewidth=3)
plt.title('PUT YOUR TITLE', fontsize=10)
plt.xlabel('PUT X LABEL')
plt.ylabel('PUT Y LABEL')
plt.xticks(
        rotation=45,
        horizontalalignment='right',
        fontweight='light',
        fontsize='8',
    )
plt.show()


# #### EXERCICE
# 
# * 1 - Plot the total_base column (barplot)
# * 2 - Plot the total_base qual-mean (dot plot)

# In[ ]:




