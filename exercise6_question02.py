#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:52:43 2018

@author: MeganHartle
"""
# This is the answer to question 2

import numpy
import pandas

#f = open("iris.csv")

data = pandas.read_csv("iris.csv")

print(data.shape)

#answer to part 1

print(data.iloc[148:,3:5])

#answer to part 2

print(data['Species'].value_counts())

#answer to part 3

print(data[data['Sepal.Width'] > 3.5].groupby('Species')['Sepal.Width'].count())

#answer to part 4

csv_to_output = "setosa.csv"
with open(csv_to_output, 'w') as file:
    for index, row in data.iterrows():
        if row['Species'] == "setosa":
            file.write(str(row['Sepal.Length']))
            file.write(', ')
            file.write(str(row['Sepal.Width']))
            file.write(', ')
            file.write(str(row['Petal.Length']))
            file.write(', ')
            file.write(row['Species'])

#answer to part 5

results = list()
for index, row in data.iterrows():
    if row['Species'] == "virginica":
        results.append(row['Petal.Length'])
        
results_mean = sum(results)/len(results)
results_min = min(results)
results_max = max(results)

print(results_mean)
print(results_min)
print(results_max)