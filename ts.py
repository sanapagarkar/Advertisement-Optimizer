import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset= pd.read_csv('Ads_CTR_Optimisation.csv')

#Implementing Thompson Sampling
import random
d=10
N=10000
ads_selected=[]
noOfRewards1 = [0]*d
noOfRewards0 = [0]*d
totalReward=0
for n in range(0,N):
    max_random = 0
    ad = 0
    for i in range (0,d):
        random_beta = random.betavariate(noOfRewards1[i]+1,noOfRewards0[i]+1)
        if(random_beta>max_random):
            max_random = random_beta
            ad=i
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    if(reward == 1):
        noOfRewards1[ad]+=1
    else:
        noOfRewards0[ad]+=1
    totalReward+=reward

# Visualising the results - Histogram 
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()