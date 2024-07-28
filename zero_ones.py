"""
https://www.codechef.com/problems/ZOOZ

"""
# cook your dish here
for t in range(int(input())):
    n = int(input())
    if n%2==0:
        print("1"+ (n-2)*"0" + "1")
    else:
        print("0"+ (n-2)*"1" + "0")
