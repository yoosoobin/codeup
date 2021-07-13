t = input()
p1 = t.find(':')
p2 = t.rfind(':')
print(t[p1+1:p2])