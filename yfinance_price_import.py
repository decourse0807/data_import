import yfinance as yf
import pandas as pd

Tickers=pd.read_csv('KOSPI_name_code.csv',encoding="cp949")


price_data=pd.DataFrame

b=0
for a in range(958):
    price_data_dummy=yf.download(Tickers['종목코드'][a]+'.KS', period='1y')
    price_data_dummy.columns=[Tickers['종목명'][a]+'_open',Tickers['종목명'][a]+'_high',Tickers['종목명'][a]+'_low',Tickers['종목명'][a]+'_close',Tickers['종목명'][a]+'_adj.close',Tickers['종목명'][a]+'_volume']
    
    if b==0:
        price_data=price_data_dummy
        b=b+1
    
    else:
        price_data=pd.concat([price_data, price_data_dummy], axis=1)
    
price_data.to_csv('price_data.csv')