h,w = map(int,input().split())
n = int(input())

D=[[0]*w for _ in range(h)]

for i in range(n):
    l,d,x,y = map(int, input().split())
    if d==0:
        for j in range(l):
            D[x-1][y-1+j]=1

    if d==1:
        for j in range(l):
            D[x - 1+j][y - 1] = 1


for i in range(h):
    for j in range(w):
        print(D[i][j],end=' ')
    print()
