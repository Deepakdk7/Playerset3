ax=int(input())
for i in range(1,ax+1):
    if ax%i==0:
        if i%2!=0:
            print(i,"",end="")
