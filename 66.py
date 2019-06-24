bx=input().split()
k=int(bx[1])
a=input().split()
b=[]
d=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    c=0
    for j in range(0,len(a)):
        if i==a[j]:
            c=c+1
    d.append(i)
    d.append(c)
for i in range(0,len(d)):
    if k==d[i]:
        print(d[i-1])
