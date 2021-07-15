a,b,c,d = map(int,input().split())
n = [a]
for i in range(d-1):
    a=n[-1]
    a = a*b+c
    n.append(a)
print(n[-1])