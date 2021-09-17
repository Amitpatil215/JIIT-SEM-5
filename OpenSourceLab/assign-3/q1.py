oldDict = {'XX': 6217, 'YY': 21321323, 'ZZ': 31245,
           'KK': 51233126, 'E': 11232, 'WW': 61321329, 'MM': 63122137, 'TT': 23312123}

newDict = dict([(value, key) for key, value in oldDict.items()])

print(oldDict)

print('\n')

print(newDict)

"""
{'XX': 6217, 'YY': 21321323, 'ZZ': 31245, 'KK': 51233126, 'E': 11232, 'WW': 61321329, 'MM': 63122137, 'TT': 23312123}

{6217: 'XX', 21321323: 'YY', 31245: 'ZZ', 51233126: 'KK', 11232: 'E', 61321329: 'WW', 63122137: 'MM', 23312123: 'TT'}

"""
