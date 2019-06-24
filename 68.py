ax=input()
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
    d.append(c)
print(max(d))
