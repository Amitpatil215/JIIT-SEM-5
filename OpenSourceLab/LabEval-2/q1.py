import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import pymongo


url = 'https://money.cnn.com/data/hotstocks/index.html'
page = urllib.request.urlopen(url)
soup = bs(page.read())
soup.prettify()
cells = []
for i in range(0, 3):
    table = soup.find_all('table')[i]
    rows = table.find_all('tr')
    output = []
    for row in rows:
        cols = row.find_all('td')
        cols = [item.text.strip() for item in cols]
        output.append([item for item in cols if item])
    df = pd.DataFrame(
        output, columns=['Company', 'Price', 'Change', '%Change'])
    df = df.iloc[1:]
    print(df)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydb"]
    mycollection = mydb["gainers_losers_db"]

# print(df)
mycollection.insert(df.to_dict('records'))

cursor = mycollection.find()
for records in cursor:
    print(records)
