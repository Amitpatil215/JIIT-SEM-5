import sys
fpath="out.tr"
fr = open(fpath,"r")
i = 0
drop=0
while 1:
    line = fr.readline();
    #print(line)
    if not line: break
    if line[0] == 'D' or line[0] == 'd':
        drop += 1

fr.close();
#print("no of drop packets ",drop)
print(drop)