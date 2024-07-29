#https://www.codechef.com/problems/WATSCORE

t = int(input())
for i in range(t):
    n = int(input())
    d = {}
    keys = []
    for j in range(n):
        p, s = map(int, input().split())
        if p in d:
            d[p].append(s)
        else:
            d[p] = [s]
        keys.append(p)
    sum = 0
    for k in set(keys):
        if keys.count(k) > 1:
            sum += max(d[k])
    print(sum)
