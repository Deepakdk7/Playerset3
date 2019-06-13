ax=list(map(int,input().split()))
bx=list(map(int,input().split()))
c=[]
for i in bx:
    if i<ax[1]:
        c.append(i)
c.sort()
for i in c:
    print(i,"",end="")
