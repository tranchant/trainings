#!/usr/bin/env python
# coding: utf-8

# # Generate csv files

# In[1]:


import os.path
import matplotlib.pyplot as plt
import pandas as pd
import sys
import pprint as pp


dir = "./fastqDirLR" #bamstat"
fastqstat_csv = "stat-merged.csv"
img_mappingob = "stat-merged.png"

# open the file merging the fastq-stat results on the whole set of samples
f=open(fastqstat_csv, "a+")
header="sample,reads,len,len_mean,qual_mean, total_bases"
f.write(header)

file_list = os.listdir(dir)
#print(file_list)

# Parsing the individual fastq-stats file
for file in file_list:

    sample =os.path.basename(file).split('.')[0]
    #print(file)
    print(sample)
    break
    newLine=f"\n{sample},"

    with open(dir+"/"+file,"r") as stat:
        for line in stat:
            line = line.rstrip()
            #print(line)

            if 'mapped (' in line or 'paired (' in line or 'singleton' in line:
                #print(line.split('(')[1].split('%')[0])
                newLine += f"{line.split('(')[1].split('%')[0]},"

        if sample in obRg:
            f.write(newLine)
        elif sample in ogRg:
            g.write(newLine)
        else:
            print(sample+"aie"+newLine)

f.close()
g.close()

