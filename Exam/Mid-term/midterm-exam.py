#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:51:15 2023

@author: leeseungjun
"""


#%% 데이터 불러오기
 
 
# 0. msf.pkl 데이터를 불러오라 (문제아님)
# Load the msf.pkl dataset to python (Not a question).
import pandas as pd
 
msf_original = pd.read_pickle('msf_midterm.pkl')
 
msf = msf_original.copy()
msf.sort_values(['date','symbol'],inplace=True,ignore_index=True)
 
 
 
 
 
#%% 계산문제
 
# 문제
print('표본내 종목수는?')
print(len(msf['symbol'].unique()))
 
 
# 문제
print('\n\n(주)아프리카TV의 월평균수익률은 얼마인가?')
print(msf.loc[msf['symbol']=='A067160','ret'].mean())
 
 
# 문제
print('\n\n(주)아프리카TV의 시총이 가장 높았던 때는 언제인가?')
print(msf.loc[msf.loc[msf['symbol']=='A067160','me'].idxmax(),'date'])
 
# 문제
print('\n\n12개월 이상 수익률 자료가 있는 종목(=월수익률 관측치가 12개 이상)의 갯수는 몇개인가? 숫자만 입력')
print((msf.groupby('symbol')['ret'].count()>=12 ).sum())
 
#문제
print('\n\n코스피 시장에서 12개월 이상 거래된 종목의 갯수는 몇개인가?')
print((msf[msf['HistExch']=='KSE'].groupby('symbol')['ret'].count()>=12).sum())
 
#문제
print('\n\n코스닥 시장 수익률이 코스피 시장 수익률을 이긴것은 몇 개월인가?')
mkt = msf.groupby(['date','HistExch'])['ret'].mean()
mkt = mkt.unstack('HistExch')
print((mkt['KSE'] < mkt['KSQ']).sum())
 
'''수업에서 배운방식 
kse = msf.loc[msf['HistExch']=='KSE'].copy()
ksq = msf.loc[msf['HistExch']=='KSQ'].copy()
print((kse.groupby('date')['ret'].mean() < ksq.groupby('date')['ret'].mean()).sum())
'''
 
 
# 문제
print('\n\n코스닥 시장평균 수익률이 코스피 시장수익률을 가장 크게 이긴 때의 코스닥 시가총액은 얼마인가?')
msf_date = msf.set_index('date')
print(msf_date.loc[(mkt['KSQ'] - mkt['KSE']).idxmax()].groupby('HistExch')['me'].sum()['KSQ'])
'''수업에서 배운방식
kse = msf.loc[msf['HistExch']=='KSE'].copy()
ksq = msf.loc[msf['HistExch']=='KSQ'].copy()
ix = (ksq.groupby('date')['ret'].mean() - kse.groupby('date')['ret'].mean()).idxmax()
print(ksq.loc[ksq['date']==ix,'me'].sum())
'''
 
 
# 문제
print('\n\n삼성전자에 4분기에만 투자했을때 누적수익률은 얼마인가?')
sam = msf[msf['symbol']=='A005930'].set_index('date')
sam['qtr'] = sam.index.quarter
print((sam['ret']/100+1).groupby(sam['qtr']).prod()-1)
 
 
# 문제: 소형주 전략
print('\n\n 매월말 시가총액이 중위수 이상인 기업에 투자하는 전략 = 대형주 전략\n\
      매월말 시가총액이 중위수 미만인 기업에 투자하는 전략 = 소형주 전략\n\
      주의: 시가총액 중위수는 매월 새로 측정해야 함. 따라서 포트폴리오는 매월 조정됨.\n\
      두 전략의 월평균 수익률 차이는 얼마(%)인가?')
msf['fret'] = msf.groupby('symbol')['ret'].shift(-1)
msf_date = msf.set_index('date') # transform을 알면 이렇게 안해도 됨
msf_date['med_me'] = msf_date['me'].groupby('date').median()
msf_date.loc[msf_date['me'] >= msf_date['med_me'],'size'] = 'B'
msf_date.loc[msf_date['me'] < msf_date['med_me'],'size'] = 'S'
print(msf_date.groupby('size')['fret'].mean().diff())
 
 
import pykrx.stock as stock
import pandas as pd
 
# 데이터다운로드
ksq = stock.get_index_ohlcv_by_date('2015-01-01', '2023-12-31', '2001', freq='d')
 
df = ksq.copy()
#문제
print('\n\n일 수익률의 표준편차는 얼마(%)인가?')
df['ret'] = df['종가'].pct_change()*100
df = df[['ret']]
print(df['ret'].std())
 
 
#문제: 삼한사온
print('\n\nK씨는 경험상 코스닥 지수가 3일 연속 상승한 다음날은 한번 더 오를 확률이 높다고 느꼈다.\
      이를 데이터를 통해 검증해보자.')
      
df['pret1'] = df['ret'].shift(1)
df['pret2'] = df['ret'].shift(2)
df['fret'] = df['ret'].shift(-1)
df = df.dropna() # 없어도 됨
 
cond = (df['pret2'] > 0) & (df['pret1'] > 0) & (df['ret'] > 0 )
df.loc[cond,'3일연속상승'] = True
df.loc[~cond,'3일연속상승'] = False # 결측치 행도 포함됨
 
print('\n\n표본기간에서 코스닥 지수가 3일 연속 상승한 날은 총 며칠인가?')
print(df['3일연속상승'].sum())
 
print('\n\n3일 연속 상승 이후 다음날에도 상승한 경우는 몇회인가?')
print((df['3일연속상승']& (df['fret'] > 0)).sum())
 
print('\n\n3거래일 연속상승일 종가에 매수하여 익일 종가에 매도하는 전략의 승률은 얼마(%)인가?')
print((df['3일연속상승']& (df['fret'] > 0)).sum()/ df['3일연속상승'].sum()*100)
 
 
print('\n\n코스닥 지수가 3일 연속 상승한 날 종가에 사서 다음날 종가에 파는 전략을 표본기간 동안 반복해보자\
      누적 수익률은 몇%인가?')   
print(((df.loc[df['3일연속상승'],'fret']/100+1).prod()-1)*100)
 
df.loc[df['3일연속상승'],'fret'].mean()

