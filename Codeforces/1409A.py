def solve(x,y):
    if x == y:
        return 0
    if x < y:
        x,y = y,x
    return int((x-y-1)/10)+1
 
t = int(input())
for i in range(t):
    x,y = map(int,input().split(' '))
    print(solve(x,y))