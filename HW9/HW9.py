# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:26:41 2019
HW 9
ME EN 2550
@author: Ryan Dalby
"""

import pandas as pd

#P4
dataP4 = pd.read_excel('HW9Data.xlsx', sheet_name = 'Problem4')
xBar = dataP4.sum().sum()/(60.0)
#UCL_L=2.114*Rbar     ## upper control limit of range
#LCL_H=0*Rbar         ## lower control limit of range 

dataP5 = pd.read_excel('HW9Data.xlsx', sheet_name = 'Problem5')


dataP6 = pd.read_excel('HW9Data.xlsx', sheet_name = 'Problem6')



