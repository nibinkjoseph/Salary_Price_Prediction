# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:39:25 2024

@author: lidya
"""

import pandas as pd

import numpy as np

df = pd.read_csv("glassdoor_jobs.csv")


#salary
#company name to text only
#location
#state
#age of company
#headquarters


#remove - 1 in salary
df.shape

df = df[df['Salary Estimate']!= '-1']

df.shape

df.head()



salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#No we need to delete K and d from salary

minus_kd  = salary.apply(lambda x: x.replace('K', '').replace('$',''))









