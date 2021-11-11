from bs4 import BeautifulSoup
import requests

req = requests.get(
    'https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")

print(soup.h1)
print(soup.h1.string)

soup.h1['class'] = 'firstHeading, mainHeading'
soup.h1.string.replace_with("Python - Programming Language")
del soup.h1['lang']
del soup.h1['id']

print(soup.h1)
print(soup.h1.string)
