ax=list(map(int,input().split()))
c=[]
for i in range(1,(ax[0]*ax[1])+1):
    if ax[0]%i==0 and ax[1]%i==0:
        c.append(i)
print(max(c))
