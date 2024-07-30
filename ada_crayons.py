#https://www.codechef.com/problems/ADACRA
t=int(input())
for _ in range(t):
    s=input()
    subcounts=[]
    c=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            c += 1
        else:
            subcounts.append([s[i],c])
            c=1
    subcounts.append([s[-1],c])   
    count=0
    for i in range(0,len(subcounts)-1,2):
        if subcounts[i][0]!=subcounts[i+1][0]:
            count=count+1
    print(count)      
