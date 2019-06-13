ax=int(input())
c=[]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(0,ax):
    for j in range(0,ax):
        if a[i]==b[j] and a[i] not in c:
            c.append(a[i])
#c=list(dict.fromkeys(c))
for i in c:
    print(i,"",end="")
