#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 05 15:23:51 2023

# Date 2023.10.05
# Author : LeeSeungjun
# St_id : 22312050
"""

import pandas as pd

# 주어진 주식 데이터
stock_data = {'APPL': [10, 5, -4, 8],
              'MSFT': [20, -9, 12, 4],
              'TSLA': [-8, 15, -7, 14]}

# DataFrame 생성 및 인덱스 이름 설정
df = pd.DataFrame(stock_data, index=[2010, 2011, 2012, 2013])
df.index.name = "연도"

# DataFrame을 stack하여 'symbol'을 열로 이동하고 결과 열의 이름을 'ret'으로 변경
df = pd.DataFrame(df.stack(), columns=['ret'])

# 인덱스를 재설정하고 '연도'와 'symbol'을 별도의 열로 가져오기
df.reset_index(inplace=True)

# 열 이름 변경 및 'date'와 'symbol'로 정렬
df.columns = ['date', 'symbol', 'ret']
df = df.sort_values(by=['date', 'symbol'])

# 변환된 DataFrame 출력
print(df)

# 'symbol'을 기준으로 오름차순 정렬
df = df.sort_values(by='symbol')

# 변환된 DataFrame 출력
print("\nsymbol 기준으로 오름차순 정렬\n")
print(df)

# 'date'을 기준으로 오름차순 정렬
df = df.sort_values(by='date')

# 변환된 DataFrame 출력
print("\ndate 기준으로 오름차순 정렬\n")
print(df)

