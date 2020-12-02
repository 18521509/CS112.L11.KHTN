n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    
    if a!=b:
        print(2*max(a,b)-1)
    else:
        print(a+b)
