def solve(x,y,k):
    return int((k*y+k+x-2)/x)+k
t = int(input())
for _ in range(t):
    x,y,k = map(int,input().split())
    print(solve(x-1,y,k))