from urllib.request import urlopen
from bs4 import BeautifulSoup
from pymongo import Connection

host = 'localhost'

database = 'lotto'
collection = 'mega_millions'

def mongo_connection():
    con = Connection(host)
    col = con[database][collection]
    return col

def main():
    col = mongo_connection()
    page_num = 1
    total_pages = 63
    while True:
        if page_num > total_pages:
            break
        page_num = str(page_num)
        soup = BeautifulSoup(urlopen('http://www.usamega.com/mega-millions-history.asp?p='+page_num).read())

    for row in soup('table')[4].findAll('tr'):
        win_dict = {}
        tds = row('td')
    if tds[1].a is not None:
        win_dict['date'] = tds[1].a.string
    if tds[3].b is not None:
        num_list = []
    #Told you we would get back to it
    number_list = tds[3].b.string.split('&middot;')
    for num in number_list:
        num_list.append(int(num))
        win_dict['numbers'] = num_list
        mega_number = tds[3].strong.string
        win_dict['mega_number'] = int(mega_number)
        col.insert(win_dict)
        page_num = int(page_num)
        page_num += 1

main()
