l1 = []
l2 = []
ans = []
n = int(input())
m = int(input())
for i in range(0, n):
    l1.append(int(input()))
for i in range(0, m):
    l2.append(int(input()))
temp1 = 0
temp2 = 0
check = False
check2 = False
while(temp1 < n and temp2 < m):
    check = False
    check2 = False
    while(check == False and temp1 < n):
        if(l1[temp1] % 2 == 1):
            check = True
            ans.append(l1[temp1])
        temp1 += 1
    while(check2 == False and temp2 < m):
        if(l2[temp2] % 2 == 0):
            check2 = True
            ans.append(l2[temp2])
        temp2 += 1
while(temp1 < n):
    if(l1[temp1] % 2 == 1):
        ans.append(l1[temp1])
    temp1 += 1
while(temp2 < m):
    if(l2[temp2] % 2 == 0):
        ans.append(l2[temp2])
    temp2 += 1
print(ans)
