ax=list(map(int,input().split()))
k=ax[1]
bx=list(map(int,input().split()))
for i in bx:
    if k==i:
        print('yes')
        break
else:
    print('no')
