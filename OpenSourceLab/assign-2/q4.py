import os

def extsort(files):
    return sorted(files, key=lambda x: os.path.splitext(x)[1])


print(extsort(['asa.c', 'dsvvsda.py', 'bweweg.py', 'bagwer.txt', 'foweggweo.txt', 'xgwewe.c']))
