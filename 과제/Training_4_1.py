#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:42:55 2023

# Date 2023.09.19
# Author : LeeSeungjun
# St_id : 22312050
"""

import pandas as pd

stock_data = {'APPL': [10, 5, -4, 8],
              'MSFT': [20, -9, 12, 4],
              'TSLA': [-8, 15, -7, 14]}

# 데이터프레임 생성
df = pd.DataFrame(stock_data, index=[2010, 2011, 2012, 2013])

print(df)

# 행 인덱스 라벨 변경
df.index = [2020, 2021, 2022, 2023]
df.index.name = "연도"

print(df)

# 열 인덱스 라벨 변경
df.columns = ['A', 'B', 'C']

print(df)






