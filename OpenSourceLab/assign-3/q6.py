str = "1,2,3,4,5,6"
noList = str.split(",")
newList = []
for i in range(len(noList)):
    no = int(noList[i].strip())
    newList.append(no)
print(newList)

"""
[1, 2, 3, 4, 5, 6]
"""