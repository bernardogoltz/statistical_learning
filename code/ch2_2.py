# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 16:43:13 2025

@author: Bernardo
"""

import pandas as pd 
import numpy as np 
import os 
import matplotlib.pyplot as plt 
import seaborn as sns 

PATH = 'C:/Users/Bernardo/Documents/ISLP/datasets/Auto.csv'

df = pd.read_csv(PATH )

"""
Quantitative
mpg
cylinders
displacement
horsepower
weight
acceleration

Qualitative
year
name 

"""

desc = df.describe().T
desc = desc[['min','max','mean','std']]

df_novo = df.drop(range(10, 86))
desc_novo = df_novo.describe().T[['min','max','mean','std']]
