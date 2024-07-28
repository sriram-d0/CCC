# https://www.codechef.com/problems/EQUALISE
# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    maxi=max(a,b)
    mini=min(a,b)
    sup=0
    flag=0
    if(a==b):
        print("Yes")
        continue
    
    while mini<maxi:
        mini*=2
         
    if mini==maxi:
        print("Yes")
    else:
        print("No")
