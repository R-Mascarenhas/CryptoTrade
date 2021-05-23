import json
import requests
import pandas as pd
import datetime, time
from tradingview_ta import TA_Handler, Interval, Exchange

f = open('coins.json','r')
coin = json.load(f)
coinext = coin['coinext'][0]
def service_url(service_name):
  return 'https://api.coinext.com.br:8443/AP/%s' % service_name


def call_get(service_name, **kwargs):
  res = requests.get(service_url(service_name), **kwargs)
  return json.loads(res.content)


def call_post(service_name, payload={}, **kwargs):
  res = requests.post(service_url(service_name),
                      json.dumps(payload), **kwargs)
  return json.loads(res.content)


def main():
  auth = call_get('authenticate', auth=('your-email', 'your-password'))
  if auth['Authenticated']:
    user_info = call_post('GetUserInfo', headers={
      'aptoken': auth['Token'],
      'Content-type': 'application/json'
    })
    print(user_info)

def obterBooks(coin = coinext['BTCBRL']):
    payload = {
        'OMSId': 1,
        'AccountId': 1,
        'InstrumentId': coin,
        'Depth': 10,
        'StartIndex': 5,
        'EndTimeStamp': 1610331168000000,
        'StartTimeStamp': 1610320368000000
        #'TradeTime': 1610331168000 #time.mktime(datetime.datetime(2020,5,10,18,52,47,874766).timetuple())
    }

    return call_post('GetL2Snapshot', payload)

data = obterBooks(coinext['BTCBRL'])
print(data[0][4])