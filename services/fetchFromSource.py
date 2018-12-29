##### fetchFromSource.py
import sqlite3, os, glob, pandas as pd, csv, requests, urllib.request, urllib, json, oauth2, datetime, time


##### Get all tickers from DB and save them into a collection (List or Dict)
class masterStockList:
    print("Entry into class masterStockList")

# Import the list from the database. The static list stockListTest to be replaced by a database call.
    def getList(self):
        # stockList = ['SNAP']
        # Connecting to the database file
        print("Entry into function getStockList")
        stockdb1 = '/Users/gagan/trendstock_data/trendstock.db'  # name of the sqlite database file
        conn01 = sqlite3.connect(stockdb1)
        sql01 = '''SELECT distinct symbol from company_list limit 20'''
        cur = conn01.cursor()
        cur.execute(sql01)
        stockInterimList = [list(i) for i in list(cur)]
        cur.close()
        conn01.close()
        symbolNumber = 0
        stockList = []
        while symbolNumber < len(stockInterimList):
            st = (stockInterimList[symbolNumber])[0]
            stockList.append(st)
            symbolNumber += 1
        print("Exit from function getStockList")
        return stockList

masterList = masterStockList()
stockList = masterList.getList()


##### For each ticker, loop through http://www.alphavantage.co API and dump file on to hard disk, and trigger loading into the DB
class fetchFromSource:

    def getWeeklyStockDetails(self):
        for s in stockList:
            stocks_url = "https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={}&apikey=SVM5&datatype=csv".format(s)
            stockfile = urllib.request.urlretrieve(stocks_url, "/Users/gagan/trendstock_data/data_files/{}.csv".format(s)) ## Parameterize the path in the long run
            print("File created for: ", s)

            def loadIntoDB(s):
                # Read file from hard drive
                print("Inside loadIntoDB for:", s)
                dailyFile = open("/Users/gagan/trendstock_data/data_files/{}.csv".format(s), "r")  # open file in current directory
                weeklyStats = []
                # Connecting to the database file
                stockdb1 = '/Users/gagan/trendstock_data/trendstock.db'  # name of the sqlite database file
                conn02 = sqlite3.connect(stockdb1)
                sql = '''INSERT OR REPLACE INTO stocks_raw(symbol, timestamp, open, high, low, close, adjusted_close, volume, dividend_amount, load_timestamp) VALUES(?,?,?,?,?,?,?,?,?,?)'''
                cur = conn02.cursor()
                for l in dailyFile:
                    weeklyStats = dailyFile.readline().split(',')
                    print(weeklyStats)
                    ts = time.time()
                    ts2 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                    cur.execute(sql, (s, weeklyStats[0],  weeklyStats[1], weeklyStats[2],
                                         weeklyStats[3], weeklyStats[4], weeklyStats[5], weeklyStats[6], weeklyStats[7], ts2))
                    conn02.commit()

                cur.close()
                conn02.close()

                return

            loadIntoDB(s)

        return


test02 = fetchFromSource()
test02.getWeeklyStockDetails()
