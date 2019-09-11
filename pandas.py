# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 03:42:38 2019

@author: humma
"""

import pandas as pd
#import os
from sklearn.ensemble import AdaBoostClassifier

#print(os.listdir(os.getcwd()))


data = pd.read_csv("check.csv")

data_list =[ list(data['Gender']), list(data['Height']), list(data['Weight']), list(data['Shoe_size']) ]
#print(data_list)

Gender = data_list[0]
Height = data_list[1]
Weight = data_list[2]
Shoe_size = data_list[3]

New_list = []

for row in range(len(Gender)):
    info = [Height[row] , Weight[row] , Shoe_size[row]]
    New_list.append(info)
    
clf = AdaBoostClassifier()

clf = clf.fit(New_list,Gender)

prediction = clf.predict([[162,58,40]])
print(prediction)