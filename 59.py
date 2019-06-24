ax=int(input())
a=(input())
a=list(a.replace(' ',''))
b=0
c=[-1]
d=[]
for i in range(0,len(a)):
    if a[i]=='0':
        c.append(i)
for i in range(0,len(c)-1):
    d.append((c[i+1]-c[i])-1)
b=sum(d)
for i in range(0,b):
    print('1',end=' ')
