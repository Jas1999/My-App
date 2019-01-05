# By:Jasman Singh Sahi 11/17/18
#alpha vantage key


import requests
import json
import datetime
import time


Token =
Alpha_link = 'https://www.alphavantage.co/query?'

def TimeSet(TimeNow):
    TimeNow = ''
    TimeNow = (datetime.datetime.now())
    if datetime.datetime.today().weekday() < 5:
        print (TimeNow)
        TimeNow = TimeNow  - datetime.timedelta(minutes=(TimeNow.minute % 10 ),  seconds=TimeNow.second, microseconds=TimeNow.microsecond)
        BusinessHoursAfter = TimeNow.replace( hour = 16)
        BusinessHoursBefore = TimeNow.replace( hour = 7)
        if  TimeNow > BusinessHoursAfter:
            TimeNow = TimeNow.replace( hour = 16, minute = 0 )

        if  TimeNow < BusinessHoursBefore:
            TimeNow = TimeNow.replace( hour = 7, minute = 0 )

        print (TimeNow)

    else:
        last_friday = (TimeNow.date()
        - datetime.timedelta(days=TimeNow.weekday())
        + datetime.timedelta(days=4))
        TimeNow = datetime.datetime.combine(last_friday, datetime.time(16))

        print(TimeNow)
        print("")
        TimeNow = str(TimeNow)
    return TimeNow


def StockInfo(Stock):
#Alpha_link ='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey='+Token
  global Token
  global Alpha_link

  Para ={
      "function" : "TIME_SERIES_INTRADAY",
      "symbol": Stock,
      "interval" : "1min",
      "outputsize": "full",
      "apikey": Token,
    }

  response = requests.get(Alpha_link, Para)

  if response.status_code == 200:
    data = response.json()
    return data

def CryptoInfo(Crypto):
#Alpha_link ='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey='+Token
  global Token
  global Alpha_link

  Para ={
      "function" : "CURRENCY_EXCHANGE_RATE",
      "from_currency": Crypto,#"BTC",
      "to_currency": "USD",
      "apikey": Token,
    }

  response = requests.get(Alpha_link, Para)

  if response.status_code == 200:
    data = response.json()
    return data

run = True
TimeNow = ""

while run:

    TimeNow = TimeSet(TimeNow)

    Stock = {"AAPL","GOOGL","TSLA"}#"AAPL"
    print("Stock Info: ")
    for i in Stock:
        StockData = StockInfo(i)
        print(i+":")
        print( StockData["Time Series (1min)"]["2018-12-31 16:00:00"] ) # yyyy,mm,dd  TimeNow "2018-12-28 16:00:00"
#"2018-12-28 16:00:00"

    Crypto = {"XRP","BTC"}#"AAPL"

    print("Crypto Info: ")
    for i in Crypto:
        CryptoData = CryptoInfo(i)
        print(i+":")
        print(CryptoData) # yyyy,mm,dd  TimeNow "2018-12-28 16:00:00"
#"2018-12-28 16:00:00"

    time.sleep(60)
    print("")
