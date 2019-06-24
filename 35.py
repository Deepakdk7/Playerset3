ax=list(input())
a=[]
b=[]
d=[]
for i in ax:
    if i not in a:
        a.append(i)
if ' ' in a:
    a.remove(' ')
for i in a:
    c=0
    for j in range(0,len(ax)):
        if i==ax[j]:
            c=c+1
    b.append(i)
    b.append(c)
    d.append(c)
x=min(d)
for i in range(0,len(b)):
    if x==b[i]:
        print(b[i-1].lower(),end=' ')
