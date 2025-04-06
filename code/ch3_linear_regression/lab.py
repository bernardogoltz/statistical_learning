# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 20:52:07 2025

@author: Bernardo
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

import statsmodels.api as sm 

from statsmodels.stats.outliers_influence import variance_inflation_factor as VIF 

from statsmodels.stats.anova import anova_lm


df = pd.read_csv('C:/Users/Bernardo/Documents/ISLP/datasets/Boston.csv')

