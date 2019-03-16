# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 21:59:05 2019

@author: Zane
"""

# Task 1
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('data_tasks.xlsx', sheet_name = 'task1')
print(df)
x_val = df.values[:,0]
y_val = df.values[:,1]
error_val = df.values[:,2]
#print(error_val)
fig = plt.figure(figsize = (8,6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.scatter(df.values[:,0], df.values[:,1], marker = 's', linewidth = 2, c = 'red')
ax1.errorbar(x_val, y_val, error_val, linewidth = 2, elinewidth = 1, c = 'gray', capsize = 5, capthick = 1)
ax1.set_xbound(0,10)
ax1.set_xlabel("Time (m)")
ax1.set_ylabel("Temperature (C)")
ax1.legend(["Temperature (C)"])

ax2.bar(x_val, y_val, yerr = error_val, capsize = 5)
ax2.set_xbound(0,10)
ax2.set_xlabel("Time (m)")
ax2.set_ylabel("Temperature (C)")
ax2.legend(["Temperature (C)"]) 




