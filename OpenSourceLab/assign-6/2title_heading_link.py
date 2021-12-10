from bs4 import BeautifulSoup
import requests

req = requests.get(
    'https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
