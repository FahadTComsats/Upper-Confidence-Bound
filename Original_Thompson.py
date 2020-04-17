#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 01:22:32 2019

@author: fahadtariq
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')


#Implememting Thompson Sampling
import random
N = 10000
d = 10
ads_selected = []
number_of_rewards_1 = [0] * d
number_of_rewards_0 = [0] * d
total_reward = 0

for n in range(0,N): #loop for rounds
    ad = 0
    max_random = 0
    for i in range(0,d): #loop for different versions of Ads
        random_beta = random.betavariate(number_of_rewards_1[i] + 1 ,number_of_rewards_0[i] + 1 )
        if random_beta > max_random:
            max_random = random_beta
            ad = i
            
    ads_selected.append(ad)
    reward = dataset.values[n ,ad]
    if reward == 1:
        number_of_rewards_1[ad] = number_of_rewards_1[ad] + 1
    else:
        number_of_rewards_0[ad] = number_of_rewards_0[ad] + 1
        
    total_reward = total_reward + reward
    
pt.hist(ads_selected)
pt.title('Histogram of ads selected')
pt.xlabel('ads')
pt.ylabel('no. of times ads was selected')
pt.show()
        
        
        
    