#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:08:19 2023

# Date 2023.09.19
# Author : LeeSeungjun
# St_id : 22312050
"""

import pandas as pd

stock_data = {'APPL': [10, 5, -4, 8],
            'MSFT': [20, -9, 12, 4],
            'TSLA': [-8, 15, -7, 14]}

# 데이터프레임 생성
df = pd.DataFrame(stock_data, index=[2010,2011,2012,2013])


# 각 주식의 4년 평균 수익률 계산 및 출력
average = df.sum(axis=0) / len(df.index)

print("[각 주식의 4년 평균 수익률]")
print(average)

# 매년 시장 평균 수익률 계산 및 출력
year_average = df.sum(axis=1) / len(df.columns)
print("\n[매년 시장 평균 수익률]")
print(year_average)

# 각 주식의 최고 수익률 계산 및 출력
df_max = df.max()
print("\n[각 주식의 최고 수익률]")
print(df_max)


