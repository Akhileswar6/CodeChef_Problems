t=int(input())
for i in range(0,t):
    x,y,z=list(map(int,input().split()))
    ak=list(x,y,z)
    list1=list(max(ak))
    list1.remove(ak)
