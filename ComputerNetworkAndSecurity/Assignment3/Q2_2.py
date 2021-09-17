import pandas as pd
import re as re
df = pd.read_csv("ComputerNetworkAndSecurity\Assignment3\exported_pcap.csv", usecols=[
                 'Info'])
contain_val = df[df['Info'].str.contains('>')]

for ind in contain_val.index:
    splitArray = contain_val['Info'][ind].split(">")
    print(splitArray[0], re.search(r'\d+', splitArray[1]).group())
    print('\n')

"""
3372   80
80   3372
3372   80
80   3372
80   3372
3372   80
80   3372
3372   80
80   3372
80   3372
3372   80
80   3372
3372   80
80   3372
3372   80
80   3372
80   3372
3372   80
80   3372
80   3371
3372   80
80   3371
3371   80
80   3372
3372   80
 """
