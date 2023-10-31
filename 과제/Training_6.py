#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:23:51 2023

# Date 2023.09.26
# Author : LeeSeungjun
# St_id : 22312050
"""

import pandas as pd

stock_data = {'APPL': [10, 5, -4, 8],
              'MSFT': [20, -9, 12, 4],
              'TSLA': [-8, 15, -7, 14]}

# 데이터프레임 생성
df = pd.DataFrame(stock_data, index=[2010, 2011, 2012, 2013])

# APPL의 수익률 시계열을 추출하여 평균 계산하기
appl_average_1 = sum(df['APPL']) / len(df['APPL'])
print("APPL의 수익률 시계열을 추출하여 평균 계산하기 : ",appl_average_1);

# 모든 기업의 연평균 수익률을 계산한 후 APPL의 결과만 추출하기
appl_average_2 = ( df.sum() / len(df) )[0]
print("\n모든 기업의 연평균 수익률을 계산한 후 APPL의 결과만 추출하기 : ",appl_average_2);

# APPL의 수익률 시계열을 추출하여 미래수익률 계산하기
appl_future_average_1 = df['APPL'].shift(-1)
print("\nAPPL의 수익률 시계열을 추출하여 미래수익률 계산하기 : ",appl_future_average_1);

# 모든 기업의 미래 수익률을 만든 후 APPL의 정보 추출하기
appl_future_average_2 = df.shift(-1)['APPL']
print("\n모든 기업의 미래 수익률을 만든 후 APPL의 정보 추출하기: ",appl_future_average_2);






