# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:00:02 2019

@author: humma
"""

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()

X = [ [181, 80, 44], [177,70,43] , [160,60,38] , [154, 54, 37] , [166,65,40] , 
   [190,90,47] , [175,64,39] , [177,70,40] , [159,55,37] , [171, 75, 42], 
   [181 , 85 , 43] ]

Y = [ 'male' , 'male' , 'female' , 'female' , 'male' , 'male' , 'female' ,
     'female' , 'female' , 'male' , 'male' ]

clf = clf.fit(X , Y)

prediction = clf.predict([[192, 101, 45.5]])

print(prediction)
