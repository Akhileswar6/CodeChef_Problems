a,b,c,x=map(int,input().split())
z=(a*b*c)
y=x**3
if z>y:
    print("Cuboid")
elif z==y:
    print("Equal")
else:
    print("Cube")
