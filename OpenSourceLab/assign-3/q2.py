dict = {
    3: 32,
    10: 231,
    2: 444,
    9: 23234,
}

sorted = sorted(dict.items(), key=lambda x: x[0])

for i in sorted:
    print(i[0], i[1])


"""
2 444
3 32
9 23234
10 231
"""
