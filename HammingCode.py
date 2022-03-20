from numpy import *
from collections import Counter

msg = [1, 0, 1, 0]
msg.reverse()
m = len(msg)
temp = msg.copy()


def requiredParity(m):
    for i in range(m):
        if(2**i >= m + i + 1):
            return i


totalParityNeeded = requiredParity(m)
codedData = []
parityPosition = [1, 2, 4, 8, 32]
for i in range(m+totalParityNeeded):
    codedData.insert(i,9)
for i in range(totalParityNeeded):
    codedData[parityPosition[i]-1] = '?'
for i in range(m+totalParityNeeded):
    if codedData[i] == 9:
        codedData[i] = temp.pop(0)

print("coded parity ?  " + str(codedData))


def calcParity(parity_pos, codedData, totalParityNeeded):
    p1 = [3, 5, 7, 9, 11]
    p2 = [3, 6, 7, 10, 11]
    p4 = [5, 6, 7]
    p8 = [9, 10, 11, 12]
    temp2 = []
    if parity_pos == 1:
        for i in range(totalParityNeeded):
            if p1[i] <= len(codedData):
                print(codedData[p1[i] - 1])
                temp2.append(codedData[p1[i] - 1])

        t = Counter(temp2)
        if t[1] % 2 == 0:
            return 0
        else:
            return 1

    if parity_pos == 2:
        for i in range(totalParityNeeded):
            if p2[i] <= len(codedData):
                print(codedData[p2[i] - 1])
                temp2.append(codedData[p2[i] - 1])

        t = Counter(temp2)
        if t[1] % 2 == 0:
            return 0
        else:
            return 1

    if parity_pos == 4:
        for i in range(totalParityNeeded):
            if p4[i] <= len(codedData):
                print(codedData[p4[i] - 1])
                temp2.append(codedData[p4[i] - 1])

        t = Counter(temp2)
        if t[1] % 2 == 0:
            return 0
        else:
            return 1

    if parity_pos == 8:
        for i in range(totalParityNeeded):
            if p8[i] <= len(codedData):
                print(codedData[p8[i] - 1])
                temp2.append(codedData[p8[i] - 1])

        t = Counter(temp2)
        if t[1] % 2 == 0:
            return 0
        else:
            return 1


for i in range(totalParityNeeded):
    codedData[parityPosition[i]-1] = calcParity(parityPosition[i], codedData, totalParityNeeded)
    print(str(parityPosition[i])+" "+ str(codedData[parityPosition[i]-1]))

print(codedData)

f = codedData.copy()
f.reverse()
print(f)