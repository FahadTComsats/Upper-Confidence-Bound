#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:49:41 2019

@author: fahadtariq
"""

import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


#Implememting UCB
import math
N = 10000
d = 10
ads_selected = []
number_of_selections = [0] * d
sum_of_reward = [0] * d
total_reward = 0

for n in range(0,N): #loop for rounds
    ad = 0
    max_bound = 0
    for i in range(0,d): #loop for different versions of Ads
        
        if number_of_selections[i] > 0:
            average_reward = sum_of_reward[i]/number_of_selections[i]
            delta_i=math.sqrt(3/2 * math.log(n +1) / number_of_selections[i])
            upper_confidence_bound = average_reward + delta_i
            
        else:
            upper_confidence_bound = 1e400
            
        if upper_confidence_bound > max_bound:
            max_bound = upper_confidence_bound
            ad = i
            
    ads_selected.append(ad)
    number_of_selections[ad] = number_of_selections[ad] + 1
    reward = dataset.values[n ,ad]
    sum_of_reward[ad] = sum_of_reward[ad] + reward
    total_reward = total_reward + reward
    
pt.hist(ads_selected)
pt.title('Histogram of ads selected')
pt.xlabel('ads')
pt.ylabel('no. of times ads was selected')
pt.show()
        
        
        
    