##### fetch_from_source.py
##### Second attempt at "Purpose-Built" Python program to pul data from the source API's
##### Getting historical stock prices from free API to get steepest declines. "The Contrarian!"
##### 12/26/2018

import sqlite3, os, glob, pandas as pd, csv, requests, urllib.request, urllib, json, oauth2, datetime, time
# The database of choice is SQLite for now.
# from alpha_vantage.timeseries import TimeSeries
# from requests.auth import HTTPDigestAuth

##### API KEY "SVM5" http://www.alphavantage.co http://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=AKAM&apikey=SVM5
##### Also get REVENUE information from Yahoo Finance


##### Get all tickers from DB and save them into a collection (List or Dict)
class masterStockList:
    print("Entry into class masterStockList")

# Import the list from the database. The static list stockListTest to be replaced by a database call.
    def getList(self):
        stockList = ['SNAP', 'PYPL']
        print("Entry into function getStockList")
        return stockList

masterList = masterStockList()
stockList = masterList.getList()


##### For each ticker, loop through http://www.alphavantage.co API and dump file on to hard disk, and trigger loading into the DB
class fetchFromSource:
    #AV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={}&apikey=SVM5'


    def getWeeklyStockDetails(self):
        for s in stockList:
            print("Stock information for: ", s)
            stocks_url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={}&apikey=SVM5&datatype=csv".format(s)
            stockfile = urllib.request.urlretrieve(stocks_url, "/Users/gagan/stocktrends/daily_files/{}.csv".format(s)) ## Parameterize the path in the long run
            print("File created for: ", s)

            def loadIntoDB(s):
                # Read file from hard drive
                dailyFile = open("/Users/gagan/trendstock/data_files/{}.csv".format(s), "r")  # open file in current directory
                weeklyStats = []
                stockdb1 = '/Users/gagan/trendstock_data/trendstock.db'  # name of the sqlite database file
                # Connecting to the database file
                conn1 = sqlite3.connect(stockdb1)
                sql = ''' INSERT INTO stocks_raw(symbol, timestamp, open, high, low, close, adjusted_close, volume, dividend_amount, load_timestamp) VALUES(?,?,?,?,?,?,?,?,?,?)'''
                cursor = conn1.cursor()
                for l in dailyFile:
                    weeklyStats = dailyFile.readline().split(',')
                    print(weeklyStats)
                    ts = time.time()
                    cursor.execute(sql, (s, weeklyStats[0],  weeklyStats[1], weeklyStats[2],
                                         weeklyStats[3], weeklyStats[4], weeklyStats[5], weeklyStats[6], weeklyStats[7], ts))
                    conn1.commit()

                cursor.close()
                conn1.close()
            return

            loadIntoDB(s)

        return


test02 = fetchFromSource()
test02.getWeeklyStockDetails()

