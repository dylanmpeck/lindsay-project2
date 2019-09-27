# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:29:44 2019

@author: user
"""

import pandas as pd
from pandas import ExcelWriter
import numpy as np
raw_data=pd.read_excel('Module 2 Project_Project Performance_v1(2).xlsx')
df= pd.DataFrame(raw_data, columns=['Quality Score','Process Days','Project Cost'])
def prob(x,y,z):
    p = np.where(x > 500 & y < 13 & z < 234000, 7,
                 np.where(x <= 500 &y<13 & z<234000, 6,
                          np.where(x > 500 & y >=13 & z<234000, 5,
                                   np.where(x <=500 & y >=13 & z<234000, 4
                                            np.where(x <=500 & y >=13 & z<234000, 3,
                                                     np.where(x<=500 & y<13 & z>=234000, 2,
                                                              np.where(x >500 & y >=13 & z>=234000, 1, 0)))))))
    return p
df['p']= prob(df['Quality Score'],df['Process Days'],df['Project Cost'])
df
