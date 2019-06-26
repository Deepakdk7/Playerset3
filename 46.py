import math
ax=float(input())
ax=math.radians(ax)
ax=math.sin(ax)
if ax>1:
    print(round(ax,1))
elif ax<1:
    print(round(ax))
