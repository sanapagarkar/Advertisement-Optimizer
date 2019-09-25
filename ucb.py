import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset= pd.read_csv('Ads_CTR_Optimisation.csv')

#Implementing UCB
import math
d=10
N=10000
ads_selected=[]
noOfSelections = [0]*d
sumsOfRewards = [0]*d
totalReward=0
for n in range(0,N):
    maxUpperBound = 0
    ad = 0
    for i in range (0,d):
        if(noOfSelections[i]>0):
            avg_reward = sumsOfRewards[i]/noOfSelections[i]
            delta_i = math.sqrt(3/2*math.log(n)/noOfSelections[i])
            upperBound = avg_reward + delta_i
        else:
            upperBound = 1e400
        if(upperBound>maxUpperBound):
            maxUpperBound = upperBound
            ad=i
    ads_selected.append(ad)
    noOfSelections[ad]+=1
    reward = dataset.values[n,ad]
    sumsOfRewards[ad]+=reward
    totalReward+=reward

# Visualising the results - Histogram 
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()