import pandas as pd
import numpy as np
import datetime as dt
import time
from pykrx import stock

##조회 기간 설정
period=[]
begin=dt.datetime(1990,1,1)
while begin < dt.datetime(2023,1,31):
    begin=begin+dt.timedelta(days=1)
    period.append(begin)



##티커 리스트 생성
ticker=set()
for a in period:
    dummy_ticker=set(stock.get_market_ticker_list(a, market='KOSPI'))
    ticker=ticker.union(dummy_ticker)
    time.sleep(0.1)

for a in period:
    dummy_ticker=set(stock.get_market_ticker_list(a, market='KOSDAQ'))
    ticker=ticker.union(dummy_ticker)
    time.sleep(0.1)


##주가 조회, 데이터 저장
data=pd.DataFrame()
for b in ticker:
    dummy_data=stock.get_market_ohlcv('19900101', '20231231', b)
    dummy_name=stock.get_market_ticker_name(b)
    dummy_data.columns=[dummy_name+'_open', dummy_name+'_high', dummy_name+'_low', dummy_name+'_close', dummy_name+'_Volume', dummy_name+'_return']
    data=pd.concat([data,dummy_data], axis=1)
    time.sleep(0.1)


##데이터 저장
data.to_csv('korea_market_19990101_20231231.csv')