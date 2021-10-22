L1 = []
L2 = []

n = int(input("No of Elements in L1: "))

print("input elements one by one for l1")

for i in range(0, n):
    each_elemets = int(input())
    L1.append(each_elemets)

m = int(input("No of Elements in L2 : "))
print("input elements one by one for l1")

for i in range(0, m):
    each_elemets = int(input())
    L2.append(each_elemets)
L = []
i = 0
j = 0
lx1 = []
lx2 = []
while(i < n):
    if(L1[i] % 2 != 0):
        lx1.append(L1[i])
    i = i+1
i = 0
while(i < m):
    if(L2[i] % 2 == 0):
        lx2.append(L2[i])
    i = i+1
i = 0
j = 0

while(i < len(lx1) and j < len(lx2)):
    L.append(lx1[i])
    L.append(lx2[j])
    i = i+1
    j = j+1

while(i < len(lx1)):
    L.append(lx1[i])
    i = i+1

while(j < len(lx2)):
    L.append(lx2[j])
    j = j+1

print(L)


"""
Enter number of elements : 4
1 2 3 4
Traceback (most recent call last):
  File "d:\Work\JIIT\Sem__5\Sem_5\OpenSourceLab\LabTest-1\q1a.py", line 8, in <module>
    each_elemets = int(input())
ValueError: invalid literal for int() with base 10: '1 2 3 4'
PS D:\Work\JIIT\Sem__5\Sem_5> python -u "d:\Work\JIIT\Sem__5\Sem_5\OpenSourceLab\LabTest-1\q1a.py"
 10
1
2
3
4
5
6
7
8
9
10
6
11
12
13
14
15
16
[1, 12, 3, 14, 5, 16, 7, 9]

"""
