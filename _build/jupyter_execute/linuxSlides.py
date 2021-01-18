#!/usr/bin/env python
# coding: utf-8

# # Discovering the linux world through jupyter 
# 
# <img style="float: left;" width="400" height="400"  src="https://www.makeitmissoula.com/wp-content/uploads/tux-antivirus.jpg">
# 
# <img style="float: center;" width="150" height="150"  src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png">
# 
# <br> 
# 
# Christine Tranchant-Dubreuil and François Sabot 

# ## The objectives
# 
# <img style="float: right;" width="500" height="500"  src="https://talentsum.com/wp-content/uploads/2014/10/ha.jpg">	 Run your own analysis using jupyter book and Linux !
#     
# 
# 
# 

# After this course, you will able to :
# 
# * Know the main Linux commands
# * Move into the Linux file tree : pwd, ls, cd, mkdir etc.
# * Connect to a Linux server and transfer data : ssh, wget
# * Work with text files: head, tail, sort, cut, wc, grep...
# * Chain and combine commands
# * Run programs from the command line
# 
# 

# # What is Linux ?
# 
# 
# <img style="float: right;" width="250" height="250"  src="https://upload.wikimedia.org/wikipedia/commons/6/69/Linus_Torvalds.jpeg">
# 
# An operating system well known for :
#  * its security and stability
#  * its frequent updates
#  * its (no) fees and openSource (mostly) softwares
#  
# **Created in 1991 by Linus Torvalds**
# 
# Linux source code **opensource** and **free** : copy, modify, redistribute
# 
# 

# # What is Linux ?
# 
# <img style="float: right;" width="500" height="500"  src="https://www.impactpc2b.com/wp-content/uploads/2018/04/images.png">
# 
# * ***Robust et multi-plateform OS*** : computer, server, android…
# 
# * ***Multi-users system*** : Several users can work simultaneously
# 
# * ***Multi-tasking system (processes/programs)***
# </br>
# Every user can run several programs at the same time
# 
# 

# # How to use Linux ?
# 
# * 2 classical ways :
# 
#   **Graphical User Interface**                                     
# <img style="float: left;" width="400" height="400" src="https://images.itnewsinfo.com/lmi/articles/grande/000000063733.jpg">
# 
# <img style="float: right;" width="400" height="400"  src="https://static.wikia.nocookie.net/mrmen/images/6/60/Mr_Happy-1A.gif">
# 

# # How to use Linux ?
# 
# 
# * 2 classical ways :
# 
#   **Graphical User Interface**     
#       
#   **Command-Line Interface through a terminal**                                     
# <img style="float: left;" width="400" height="400" src="https://upload.wikimedia.org/wikipedia/commons/2/29/Linux_command-line._Bash._GNOME_Terminal._screenshot.png">
# 
# <img style="float: right;" width="200" height="200"  src="https://pbs.twimg.com/media/EHueI1AU4AADeic.jpg">
# 

# # How to use Linux ?
# 
# 
# * a new and alternative ways :
# 
#   **jupyter book**                       
# <img style="float: left;" width="500" height="500"  src="https://user-images.githubusercontent.com/10065489/27256117-67ec0306-537a-11e7-84aa-dbf86e0608f7.png">
# 
# <img style="float: right;" width="500" height="500" src="https://docs.thevirtualbrain.org/_images/ipy_notebook_home.png">
# 
# 
# 

# # Why using Linux ?
# 
# 
# * Numerous fast and powerful programs
# 
# * Easy to link commands and programs (workflow)
# 
# * Numerous bioinformatics softwares available 
# 
# * 90% of servers on Linux
# 

# # Why using Linux ?
# 
# Need to pratice!!!
# 
# **Important investissments to have good results !!!**
#                      
# <img style="float: left;" width="500" height="500"  src="https://www.mesfinancesperso.com/blog/wp-content/uploads/2014/08/le-grand-saut.jpg">
# 
# 

# # First steps on Linux
# 
# Commands for moving around the file system and manipulating files/folders
# 

# # First steps on Linux
# 
# Commands for moving around the file system and manipulating files/folders
# 
# command [ -options] [ arguments ]
# 

# # Your first command _pwd_
# 
# **pwd** print the name of the curent directory (the full path)

# In[1]:


get_ipython().run_cell_magic('bash', '', 'pwd')


# In[2]:


get_ipython().run_line_magic('load_ext', 'rpy2.ipython')


# In[3]:


get_ipython().run_cell_magic('R', '', 'X=c(1,2,4,5,7)\nmean(X)')


# In[ ]:




