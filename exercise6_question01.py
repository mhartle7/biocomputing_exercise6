#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:00:26 2018

@author: MeganHartle
"""

# This is the answer to question #1
# Originally I was going to use an index but since I have used C++ and I have used
# for loops I thought it might be easier to use one to solve this problem 

Numberlines=10
f=open("iris.csv")
for i in range(Numberlines):
    line=f.next().strip()
    print line
f.close()