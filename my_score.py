#https://www.codechef.com/problems/WATSCORE

for i in range(int(input())):
    n=int(input())
    a=[0]*8
    for j in range(n):
        x,y=map(int,input().split())
        if x<=8:
            a[x-1]=max(a[x-1],y)
    print(sum(a))
