a,b,c = map(int, input().split())
list_ = [a,b,c]
for i in list_:
    if i %2 == 0:
        print('even')
    else:
        print('odd')