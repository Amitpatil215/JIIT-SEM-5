import numpy as geek

# input array contains only numeric character
in_arr = geek.array(['2', 'ab','234','word','123456'])

out_arr = geek.char.isnumeric(in_arr)
new=[]
for x in range(out_arr.length):
    if(out_arr[x]==True):
        new.append(in_arr[x])

print(new)