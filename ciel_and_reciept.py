#https://www.codechef.com/problems/CIELRCPT

t=int(input())
l=[1,2,4,8,16,32,64,128,256,512,1024,2048]
l.sort(reverse=True)
for _ in range(t):
    n=int(input())
    c=0
    for i in l:
        while i<=n:
            c=c+1
            n=n-i
    print(c)  
    


