ax=list(map(int,input().split()))
a=ax[0]
b=ax[1]
for i in range(0,a):
    if (b**i)==a:
        print('yes')
        break
else:
    print('no')
