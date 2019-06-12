ax=input()
c=[]
for i in ax:
    if i.islower()==True:
        c.append(i.upper())
    elif i.isupper()==True:
        c.append(i.lower())
for i in c:
    print(i,end="")
