#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:31:09 2023

# Date 2023.10.10
# Author : LeeSeungjun
# St_id : 22312050
"""

from pykrx import stock
import pandas as pd

# 코스피와 코스닥 데이터를 다운로드
kse_df = stock.get_index_ohlcv_by_date("20220101","20221231","1001",freq='m');

ksq_df = stock.get_index_ohlcv_by_date("20220101","20221231","2001",freq='m');

# 각 데이터프레임에 월 수익률 컬럼을 추가
kse_df['월 수익률'] = ((kse_df['종가'].copy().shift(-1) / kse_df['종가'].copy() -1)*100).shift(1)

ksq_df['월 수익률'] = ((ksq_df['종가'].copy().shift(-1) / ksq_df['종가'].copy() -1)*100).shift(1)

# 코스피와 코스닥의 월간수익률을 컬럼으로 가지는 새로운 데이터프레임 생성
df = pd.DataFrame()

df['kse'] = kse_df['월 수익률'].copy()
df['ksq'] = ksq_df['월 수익률'].copy()






