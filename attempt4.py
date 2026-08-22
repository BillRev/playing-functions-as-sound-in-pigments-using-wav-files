#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: wjreveley
"""

import pickle
import math


with open("sinwaves.pkl", "rb") as file:
    allwaves = pickle.load(file)
    



'''choose number of waveforms'''
number_of_waveforms = 512

'''choose function'''
def function(x):
    return math.sin(x)

'''choose interval'''
a = 0
b = 2*math.pi

xvalues = []
for i in range(0, number_of_waveforms):
    xvalues.append(a+(i*(b-a))/(number_of_waveforms-1))
    
yvalues = []
for i in xvalues:
    yvalues.append(function(i))
  
    
'''makes all values positive by shifting them up''' 
#positiver = 0
#if min(yvalues) < 0:
positiver = -1*min(yvalues)
   
posyvalues = []
for i in yvalues:
    posyvalues.append(i+positiver)



'''scales so that all values are between 1 and 50 but still holds same shape'''
scaledyvalues=[]
for i in posyvalues:
    scaledyvalues.append(1+i*49/max(posyvalues))

rndyvalues = []
for i in scaledyvalues:
    rndyvalues.append(round(i))
'''this now corresponds to how many sine waves each waveforms gets'''
print(rndyvalues)

x= []
for i in rndyvalues:
    x += allwaves[i-1]
    

'''choose name of txt file'''
with open("sinx512.txt", "w") as file:
    for number in x:
        file.write(str(number) + "\n")
        


'''choose name of wav file'''
import soundfile as sf

sf.write("cosx512.wav", x, 44100, subtype="PCM_24")