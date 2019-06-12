import math
ax=list(map(int,input().split()))
s=c=0
for i in range(ax[0],ax[1]+1):
    s=math.sqrt(i)
    if s*s==i:
        c=c+1
print(c)
