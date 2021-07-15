n = int(input())
numbers = list(map(int,input().split()))
small = numbers[0]
for i in range(n):
    if numbers[i] <= small:
        small = numbers[i]
    else:
        pass
print(small)