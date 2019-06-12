ax=int(input())
for i in range(2,ax):
    if ax%i==0:
        print('yes')
        break
else:
    print('no')
