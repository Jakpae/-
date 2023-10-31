#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:31:12 2023

# Date 2023.10.12
# Author : LeeSeungjun
# St_id : 22312050
"""

from pykrx import stock
import pandas as pd

# 코스피와 코스닥 데이터를 다운로드
kse_df = stock.get_index_ohlcv_by_date("20210101","20221231","1001",freq='m');

ksq_df = stock.get_index_ohlcv_by_date("20210101","20221231","2001",freq='m');

# 각 데이터프레임에 월 수익률 컬럼을 추가
kse_df['월 수익률'] = ((kse_df['종가'].copy().shift(-1) / kse_df['종가'].copy() -1)*100).shift(1)

ksq_df['월 수익률'] = ((ksq_df['종가'].copy().shift(-1) / ksq_df['종가'].copy() -1)*100).shift(1)

# 연도 정보를 가지는 컬럼 생성

kse_df['year'] = kse_df.index.year

ksq_df['year'] = ksq_df.index.year

print("-- 연도별 코스피 평균 수익률 --\n",kse_df.groupby('year')['월 수익률'].mean())

print("\n-- 연도별 코스닥 평균 수익률 --\n",ksq_df.groupby('year')['월 수익률'].mean())

print("\n-- 연도별 코스피 최고 수익률 --\n",kse_df.groupby('year')['월 수익률'].max())

print("\n-- 연도별 코스닥 최고 수익률 --\n",ksq_df.groupby('year')['월 수익률'].max())

kse_df['month'] = kse_df.index.month

ksq_df['month'] = ksq_df.index.month

print("\n-- 연도별 코스피 최고 수익률 --\n",kse_df.loc[kse_df.groupby('year')['월 수익률'].idxmax(), ['month']])

print("\n-- 연도별 코스닥 최고 수익률 --\n",ksq_df.loc[ksq_df.groupby('year')['월 수익률'].idxmax(), ['month']])

# 각 연도별 코스피 최고 월 수익률과 해당 월에 대한 코스닥 수익률 찾기
kse_max_returns = kse_df.groupby('year')['월 수익률'].max()
kse_max_returns_indices = kse_df.groupby('year')['월 수익률'].idxmax()
ksq_max_returns = ksq_df.loc[kse_max_returns_indices, '월 수익률']

# 결과를 표시할 데이터프레임 생성
result_df = pd.DataFrame({'코스피 최고 수익률': kse_max_returns, '해당 월 코스닥 수익률': ksq_max_returns})

print("-- 연도별 코스피 최고 수익률과 해당 월에 대한 코스닥 수익률 --\n", result_df)



