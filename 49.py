ax=int(input())
if(ax>=-2**15+1  and ax<=2**15+1):
    print ("INT")
elif ax>=-2**31+1 and ax<=2**31+1:
    print("LONG")  
else:
    print("LONG LONG")
