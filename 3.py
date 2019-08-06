ax,bx=input().split()
c=l=0
l=min(len(ax),len(bx))
v=max(len(ax),len(bx))
for i in range(l):
    if ax[i]==bx[i]:
        c=c+1
    else:
        break
print(v-c)
