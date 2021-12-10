import requests
from pymongo import MongoClient, collation
from bs4 import BeautifulSoup

# make a request to the site and get it as a string
markup = requests.get(f'http://quotes.toscrape.com/').text

# pass the string to a BeatifulSoup object
soup = BeautifulSoup(markup, 'html.parser')

# this will hold all the quotes
quotes = []

# now we can select elements
for item in soup.select('.quote'):
    quote = {}
    quote['text'] = item.select_one('.text').get_text()
    quote['author'] = item.select_one('.author').get_text()

    # get the tags element
    tags = item.select_one('.tags')

    # get each tag text from the tags element
    quote['tags'] = [tag.get_text() for tag in tags.select('.tag')]
    quotes.append(quote)

# print(quotes)


# creation of MongoClient
client = MongoClient()

# Connect with the portnumber and host
client = MongoClient("mongodb://localhost:27017/")

# Access database
mydatabase = client["sname_of_the_database"]

# Access collection of the database
mycollection = mydatabase["myTable"]

# dictionary to be added in the database
rec = quotes

# inserting the data in the database
# rec = mydatabase.myTable.insert_many(rec)

# To find() all the entries inside collection name 'myTable
cursor = mycollection.find()
for record in cursor:
    print(record)
