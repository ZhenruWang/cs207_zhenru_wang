"""
Created on Tue Oct  1 12:56:53 2019

@author: zhenrumacpro
""" 
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

def languages(filename):
    file = open(filename)
    lists = file.read().splitlines()
    c_dict = Counter(lists)
    print(c_dict)
    x_coords = np.arange(len(c_dict.keys()))
    freqs = c_dict.values()
    labels = c_dict.keys()
    #print(x_coords)
    plt.bar(x_coords,freqs)
    plt.xticks(x_coords,labels)
    file.close() 
    return c_dict

languages('languages.txt')