#!/usr/bin/python

import os,sys
from scipy import stats
import numpy as np
from sklearn.preprocessing import normalize



data = np.loadtxt('/Users/Carol/Desktop/cleaned.txt', delimiter='\t', skiprows=1, usecols=range(1,128))

Normalized = normalize(data, norm='l1', axis=1)

print(Normalized)
#"""axis = 0 indicates, normalize by column and if you are 
#interested in row normalization just give axis = 1"""


#with open("/Users/Carol/Desktop/norm.txt", "w") as output:
 #output.write(Normalized)

np.savetxt('result.csv',(Normalized),fmt="%s")