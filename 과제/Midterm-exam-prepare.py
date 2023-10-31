#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:00:16 2023

@author: leeseungjun
"""

import pandas as pd
msf = pd.read_pickle('msf.pkl')

# 0. 전반적 탐색
msf.info()
msf['HistExch'].unique()
msf.head(10)
# monthly stock file: msf
# daily stock file: dsf


# 1. data, symbol 오름차순으로 정렬하라 (인덱스라벨을 0부터 재설정하라)
msf.sort_values(['date','symbol'],ignore_index=True)
 
# 2. 몇개의 기업이 있는가? 

len(msf['symbol'].unique())
msf['symbol'].unique().size
 
# 3. 표본 기간은 언제부터 언제까지인가?

msf['date'].unique().min()
msf['date'].unique()[0]
msf['date'].unique().max()
msf['date'].unique()[-1]

# 4. 종목별 평균 수익률과 평균 시가총액의 기초통계량(=횡단면 기초통계량)을 확인해보자.

msf.groupby('symbol')[ ['ret','me'] ].mean().describe()

 
# 5. 삼성전자(네이버에서 코드 검색)의 월 평균 수익률은 얼마인가?
msf.loc[msf['symbol'] == 'A005930','ret'].mean()

msf_sym = msf.set_index('symbol') 
msf_sym.loc[ 'A005930', 'ret'].mean()

# 6. 월평균 수익률이 가장 높은 종목은 무엇인가
msf.groupby('symbol')['ret'].mean().idxmax()
 
# 7. 1년 이상 거래된 종목 중 월평균 수익률이 가장 높은 종목은 무엇인가?
 
msf_sym['count'] = msf.groupby('symbol')['ret'].count()
ix = msf_sym.loc[msf_sym['count']>12].copy().groupby('symbol')['ret'].mean().idxmax()



# 8. 위 종목의 변동성은 얼마인가?

msf_sym.loc[ix,'ret'].std()
msf.loc[msf['symbol']==ix,'ret'].std()
 
# 9. 월별 시장 동일가중 평균 수익률을 구하여라

mkt = msf.groupby('date')['ret'].mean()
 
# 10. 동일가중 시장포트폴리오에 투자했다고 가장하자. 매년 분기별 누적수익률을 구하라

mkt['year'] = mkt.index.year


# 11. 분기별 누적수익률의 기초통계량을 확인하라. 몇분기 수익률이 평균적으로 가장 좋은가?