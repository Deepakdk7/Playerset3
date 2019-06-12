ax=int(input())
a=list(map(int,input().split()))
t=list(a)
a.sort()
if a==t:
    print('yes')
else:
    print('no')
