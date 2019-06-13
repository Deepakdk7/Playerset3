ax=list(map(int,input().split()))
bx=list(map(int,input().split()))
x=ax[1]
c=0
for i in range(0,len(bx)):
    for j in range(i+1,len(bx)):
        if bx[i]+bx[j]==x:
            c=1
            break
if c==1:
    print('yes')
else:
    print('no')
