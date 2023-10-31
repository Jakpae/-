#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:03:03 2023

@author: leeseungjun
"""

import pandas as pd

stock_data = {
    'AAPL': [10, 5, -4, 8],
    'MSFT': [20, -9, 12, 4],
    'TSLA': [-8, 15, -7, 14]
}

# 데이터프레임 생성
df = pd.DataFrame(stock_data, index=[2010, 2011, 2012, 2013])

# DataFrame을 stack하여 'symbol'을 열로 이동하고 결과 열의 이름을 'ret'으로 변경
df = pd.DataFrame(df.stack(), columns=['ret'])

# 인덱스를 재설정하고 '연도'와 'symbol'을 별도의 열로 가져오기
df.reset_index(inplace=True)

# 열 이름 변경 및 'date'와 'symbol'로 정렬
df.columns = ['date', 'symbol', 'ret']
df = df.sort_values(by=['date', 'symbol'])

# 각 기호별로 첫 번째 날의 값을 기준으로 누적 퍼센트 변화 계산
df['fv'] = (df['ret'] / 100 + 1).groupby(df['symbol']).cumprod()

df['avgret'] = df.groupby('symbol')['ret'].cumsum() / 4







