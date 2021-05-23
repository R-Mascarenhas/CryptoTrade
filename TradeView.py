# -*- coding: utf-8 -*-
"""
Created on Sat May 22 20:07:12 2021

@author: Rafael

pip install tradingview_ta

https://pypi.org/project/tradingview-ta/
"""

from coins import *
from tradingview_ta import TA_Handler, Interval, Exchange


def GET_RECOMMENDATION(cryptocurrency, interval = Interval.INTERVAL_5_MINUTES):
    handler = TA_Handler(
            symbol = cryptocurrency.SYMBOL,
            screener = SCREENER,
            exchange = cryptocurrency.Exchange,
            interval = interval
            )

    coin = handler.get_analysis()
    
    if coin.summary["RECOMMENDATION"] == "STRONG_BUY":
        RECOMMENDATION = "BUY"
    elif coin.summary["RECOMMENDATION"] == "STRONG_SELL":
        RECOMMENDATION = "SELL"
    else:
        RECOMMENDATION = "NEUTRAL"
        
    return {"COIN":cryptocurrency.Name, "RECOMMENDATION": RECOMMENDATION, "VALUE":coin.indicators['close'], "TIME":str(coin.time)}


"""
def Recommendation(cryptocurrency):
    coin = GET_RECOMMENDATION(cryptocurrency)
    if coin.summary["RECOMMENDATION"] == "STRONG_BUY":
        RECOMMENDATION = "BUY"
    elif coin.summary["RECOMMENDATION"] == "STRONG_SELL":
        RECOMMENDATION = "SELL"
    else:
        RECOMMENDATION = "NEUTRAL"
    return {"RECOMMENDATION": RECOMMENDATION, "VALUE":coin.indicators['close'], "TIME":str(coin.time)}

"""    
#File.Write("BITCOIN.txt", BuyOrSell(Bitcoin))
"""

coin = GET_RECOMMENDATION(Bitcoin, '1h')

print("Oscilators recommendation: ", coin.oscillators['RECOMMENDATION'])
print("Moving Averages Recommendation: ", coin.moving_averages['RECOMMENDATION'])

print(coin.summary)

MACD = coin.indicators['MACD.macd']
SIGNAL = coin.indicators['MACD.signal']
print("MACD: " , MACD)
print("SIGNAL: " , SIGNAL)

if MACD > SIGNAL and abs(MACD) > abs(SIGNAL)*1.15 and coin.summary["RECOMMENDATION"] == "STRONG_BUY":
    print("BUY")
else:
    print("SELL")

"""


