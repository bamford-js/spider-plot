# -*- coding: utf-8 -*-
"""
--- SPIDER GRAPH ---

Spider graph. Does whatever a spider graph does.

Created on Tue Nov 26 09:27:54 2024
@author: bamford-js
"""

import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data

df = pd.DataFrame({
    'group': ['A','B','C'],
    'Factor 1': [5,8,16],
    'Factor 2': [18,3,10],
    'Factor 3': [8,13,4],
    'Factor 4': [16,7,3],
    'Factor 5': [5,2,7]
    })

# ------- PART 1: Create background

# number of variables
categories=list(df)[1:]
N = len(categories)

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

# Draw one axe per variable + add labels
ax.tick_params(pad=10)
plt.xticks(angles[:-1], categories)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([5,10,15], ["5","10","15"], color="grey", size=7)
plt.ylim(0,20)

# ------- PART 2: Add plots

colours = ['b','r','r'] 

for i in range(len(df[['group']])):
    values=df.loc[i].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=df.loc[i,'group']) 
    ax.fill(angles, values, colours[i], alpha=0.1)

# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 0.4))

# Show the graph
plt.show()