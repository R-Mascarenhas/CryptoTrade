# -*- coding: utf-8 -*-
"""
Created on Sun May 23 01:07:48 2021

@author: Rafael
"""

import TradeView as TV
import File
from coins import *
import Telegram


Value = File.Read("Value.txt") #{"BRL":{"Bitcoin":1000, "Ethereum":1000, "Litecoin":1000, "Dogecoin":1000, "Ripple":1000, "BitcoinCash": 1000, "ChainLink": 1000, "Cardano": 1000, "EOS": 1000, "Stellar": 1000},
         #"CRYPTO":{"Bitcoin":0, "Ethereum":0, "Litecoin":0, "Dogecoin":0, "Ripple":0, "BitcoinCash": 0, "ChainLink": 0, "Cardano": 0, "EOS": 0, "Stellar": 0}}
Recommendation = File.Read("Recommendation.txt") #{"Bitcoin":"NEUTRAL", "Ethereum":"NEUTRAL", "Litecoin":"NEUTRAL", "Dogecoin":"NEUTRAL", "Ripple":"NEUTRAL", "BitcoinCash": "NEUTRAL", "ChainLink": "NEUTRAL", "Cardano":"NEUTRAL", "EOS":"NEUTRAL", "Stellar":"NEUTRAL"}
CoinPath = "coinLogs/"
fee = 0.5/100


def makeOrder(crypto):
    if Recommendation[crypto['COIN']] == "SELL":
        Sell(crypto, Value['CRYPTO'][crypto['COIN']])
        Message = "SELL " + crypto['COIN'] + ' @ ' +  Value['CRYPTO'][crypto['COIN']] + eval(crypto['COIN']).SYMBOL[:-3]
        Telegram.sendMessage(Message=Message)
    elif Recommendation[crypto['COIN']] == "BUY":
        Buy(crypto, Value['BRL'][crypto['COIN']])
        Message = "BUY " + crypto['COIN'] + ' @ ' +  Value['BRL'][crypto['COIN']] + "BRL"
        Telegram.sendMessage(Message=Message)

def Buy(crypto, value):
    print("BUY ", crypto["COIN"])
    Value["CRYPTO"][crypto["COIN"]] = (value*(1-fee))/crypto['VALUE']
    Value["BRL"][crypto["COIN"]] = 0
    crypto["CRYPTO"] = Value["CRYPTO"][crypto["COIN"]]
    fileName = CoinPath + crypto["COIN"] + ".txt"
    File.Write(fileName, crypto)

def Sell(crypto, value):
    print("SELL ", crypto["COIN"])
    Value["BRL"][crypto["COIN"]] = (value*crypto["VALUE"])*(1-fee)
    Value["CRYPTO"][crypto["COIN"]] = 0
    crypto["BRL"] = Value["BRL"][crypto["COIN"]]
    fileName = CoinPath + crypto["COIN"] + ".txt"
    File.Write(fileName, crypto)
    
def BuyOrSell(cryptocurrency):
    if cryptocurrency["RECOMMENDATION"] != "NEUTRAL" and cryptocurrency["RECOMMENDATION"] != Recommendation[cryptocurrency["COIN"]]:
        Recommendation[cryptocurrency["COIN"]] = cryptocurrency["RECOMMENDATION"]
        makeOrder(cryptocurrency)
        File.Write("Value.txt", Value)
        File.Write("Recommendation.txt", Recommendation)
    

def Start():
    BALANCE = 0.0
    for coin in Value["BRL"].keys():
        print ("Analysing ", coin, "-> Market: ", end='')
        try:
            cryptocurrency = TV.GET_RECOMMENDATION(eval(coin), interval = "5m")
        except Exception as inst:
            print(inst, '\n')
            return
        print(cryptocurrency["VALUE"], 'BRL; Wallet: ',  round(Value["BRL"][cryptocurrency["COIN"]],2), " BRL + ", Value["CRYPTO"][cryptocurrency["COIN"]], ' ' ,eval(coin).SYMBOL[:-3])
        BuyOrSell(cryptocurrency)
        BALANCE += cryptocurrency["VALUE"] * Value["CRYPTO"][cryptocurrency["COIN"]] + Value["BRL"][cryptocurrency["COIN"]]
    print("BALANCE: R$", round(BALANCE,2), '\n')



    


