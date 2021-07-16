mirror = []

for i in range(10):
    mirror.append(list(map(int,input().split())))

x,y = 1,1

while True:
    if (mirror[x][y]==0):
        mirror[x][y]=9
    elif(mirror[x][y]==2):
        mirror[x][y]=9
        break
    if((mirror[x][y+1]==1 and mirror[x+1][y]==1)):
        break

    if (mirror[x][y+1] != 1):
        y +=1
    elif (mirror[x+1][y] !=1):
        x +=1

for i in range(10):
    for j in range(10):
        print(mirror[i][j],end=' ')
    print()

