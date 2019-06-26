ax=input().split()
q=int(ax[0])
p=q//2
e=0
a=int(ax[1])
c=max(a,q)
for i in range(0,25):
    for j in range(0,c):
        if i*j==a and i+j==p:
            e=1
            break
if e==1:
    print('yes')
else:
    print('no')
