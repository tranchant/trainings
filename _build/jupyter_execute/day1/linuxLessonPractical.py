#!/usr/bin/env python
# coding: utf-8

# # First steps on Linux
# 
# Commands for *moving around the file system* and *manipulating files/folders*
# 
# <img style="float: left;" width="800" height="800"  src="https://upload.wikimedia.org/wikipedia/commons/f/f3/Standard-unix-filesystem-hierarchy.svg">
# 

# # Linux command syntax
# 
# command [ -options] [ arguments ]
# 

# # Your first command _pwd_
# 
# **pwd** print the name of the curent directory (the full path)

# In[1]:


get_ipython().run_line_magic('cd', '/home/christine/Documents/Formation/TS/Home')
get_ipython().run_line_magic('pwd', '')


# Kezako ?
# 
# Add img arbo

# # 2nd command _ls_
# 
# * without argument : list all the files in the current directory (by default)
# 

# In[2]:


get_ipython().run_line_magic('ls', '')


# Kezako ?
# 
# Add img arbo

# # 2nd command + option _ls -l_
# 
# ls -l : _list files with more information about each file_ (long)

# In[3]:


get_ipython().run_line_magic('ls', '-l')


# # 2nd command + argument
# 
# with argument <=> directory path

# In[4]:


get_ipython().run_line_magic('ls', 'fastqDirLR')


# ### EXERCICE : list all the files into fastqDirSR directory (format long)

# In[5]:


get_ipython().run_line_magic('ls', 'TO_BE_COMPLETED')


# # A few Basic Commands
# 
# How to get help about one command
# 
# * with the ’option --help ou -h     
# * with the command man       

# ### EXERCICE : use the --help option or tha man command with ls

# In[6]:


get_ipython().run_line_magic('TYPE', 'YOUR COMMAND')


# In[3]:


get_ipython().run_line_magic('load_ext', 'rpy2.ipython')


# In[4]:


get_ipython().run_cell_magic('R', '', 'X=c(1,2,4,5,7)\nmean(X)')


# In[ ]:




