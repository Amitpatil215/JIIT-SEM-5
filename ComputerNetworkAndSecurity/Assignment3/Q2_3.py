import pandas as pd

df = pd.read_csv("ComputerNetworkAndSecurity\Assignment3\exported_pcap.csv", usecols=[
                 'Info', 'Protocol'])
contain_val = df[df['Protocol'].str.contains('HTTP')]
print(contain_val)

"""
    Protocol                                               Info
3       HTTP                       GET /download.html HTTP/1.1
17      HTTP  GET /pagead/ads?client=ca-pub-2309191948673629...
26      HTTP                       HTTP/1.1 200 OK  (text/html)
37  HTTP/XML                                   HTTP/1.1 200 OK

"""