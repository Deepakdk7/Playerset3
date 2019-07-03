ax=int(input())
c=0
for i in range(ax):
    a,b=list(map(int,input().split()))
    if a<b:
        c=c+1
print(c)
