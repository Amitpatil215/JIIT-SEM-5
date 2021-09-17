import glob
finalList = []
files_list = glob.glob("OpenSourceLab/assign-3/*.txt")
for file_elem in files_list:
    with open(file_elem, "r") as f:
        finalList.append(f.read())
print(finalList)

"""
['This text is from file 1', 'appendeing text from file 2 , ahh pointer came here']
"""