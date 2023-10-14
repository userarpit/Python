# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:36:23 2023

@author: HP
"""

from scipy import stats

speed=[12,86,45,76,12,56,100]

x = stats.mode(speed)
print(x)
