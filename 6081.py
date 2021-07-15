a =input()
for i in range(1,16):
    print(a,'*','%X'%i,'=','%X'%(int(a,16)*i),sep='')