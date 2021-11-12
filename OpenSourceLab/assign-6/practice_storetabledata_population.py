from bs4 import BeautifulSoup
import urllib.request
import pymongo


url = 'https://worldpopulationreview.com/country-rankings/olympic-medals-by-country'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
soup.prettify()

table = soup.find("div", {"class": "jsx-1911055634"})

cells = []
for row in table.findAll("tr"):
    result = row.findAll("td")
    if len(result) == 6:
        dic = {}
        dic["Country"] = result[0].get_text()
        dic["Gold"] = result[1].get_text()
        dic["Silver"] = result[2].get_text()
        dic["Bronze"] = result[3].get_text()
        dic["Total"] = result[4].get_text()
        dic["Population"] = result[5].get_text()
        cells.append(dic)

print(cells)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.insert_many(cells)
print(x)
