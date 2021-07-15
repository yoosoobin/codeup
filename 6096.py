d = []
for i in range(19):
    a = list(map(int,input().split()))
    d.append(a)

n = int(input())
for i in range(n):
    r,c = map(int,input().split())
    for i in range(19):
        if d[r-1][i] ==0:
            d[r-1][i]=1
        else:
            d[r-1][i]=0
    for j in range(19):
        if d[j][c-1]==0:
            d[j][c-1] = 1
        else:
            d[j][c-1] = 0
cnt = 0
for i in range(19):
    for j in range(19):
        if cnt <18:
            print(d[i][j], end=' ')
            cnt +=1
        else:
            print(d[i][j], end='\n')
            cnt = 0