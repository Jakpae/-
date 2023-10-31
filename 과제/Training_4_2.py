#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:52:13 2023

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

# 행 인덱스 라벨 변경
df.index.name = "연도"

print(df)

# '연도'를 하나의 열로 빼내고, 인덱스를 초기화
df.reset_index(inplace=True)

print(df)

# '연도'를 다시 인덱스로 설정
df.set_index('연도', inplace=True)

print(df)

# MSFT의 수익률 오름차순으로 데이터를 정렬
df.sort_values(by='MSFT', ascending=True, inplace=True)

print(df)

# '연도'순으로 데이터를 정렬
df.sort_index(inplace=True)

print(df)

# 열을 내림차순으로 정렬
df.sort_index(axis=1, ascending=False, inplace=True)

print(df)

print(df.shift(-1))



