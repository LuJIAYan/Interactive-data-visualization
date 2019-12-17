# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:20:44 2019

@author: ljy
"""

import pandas as pd
df = pd.read_csv('D:\1好好学习天天向上\数据可视化产品\Interactive-data-visualization\data.csv',encoding='gbk')
print(type(df),df['name'].dtype) # 查看df类型，查看df中一列的数值类型
df.head()