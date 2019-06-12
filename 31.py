ax=input()
c=d=0
for i in ax:
    if i=='(':
        c=c+1
    if i==')':
        d=d+1
if c==d:
    print('yes')
else:
    print('no')
