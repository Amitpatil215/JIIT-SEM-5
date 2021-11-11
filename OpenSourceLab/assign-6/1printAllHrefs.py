from bs4 import BeautifulSoup
import requests

url = "google.com"
r = requests.get("https://" + url)
data = r.text
soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    print(link.get('href'))
