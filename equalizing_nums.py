#https://www.codechef.com/problems/EQLZING
# cook your dish here
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a==b:
        print("Yes")
        continue
    if (a%2==0 and b%2==0) or (a%2!=0 and b%2!=0):
        print("Yes")
    else:
        print("No")
