n = int(input())
pos = []
for i in range(n):
    p = list(map(int,input().split()))
    pos.append(p)

d=[[0 for j in range(19)] for i in range(19)]

for i,j in pos:
    d[i-1][j-1]=1

ct = 0
for i in d:
    for j in i:
        ct += 1
        if ct ==19:
            print(j,end='\n')
            ct =0
        else:
            print(j,end=' ')

