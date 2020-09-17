def divisors(n):
    a = []
    for i in range(1,n+1):
        if n%i == 0:
            a.append(i)
    return a
F = [None]*51
for i in range(1,51):
    F[i] = divisors(i)
 
def cal(n,x,y,t):
    if (y-x)/t > n-1:
        return
    start = x%t
    if start ==0:
        start += t
    if (n-1)*t >= y:
        return start
    else:
        return y-(n-1)*t
 
def solve(n,x,y):
    end,start,t = 9999999,0,0
    global F
 
    for i in F[y-x]:
        s = cal(n,x,y,i)
        if s is None:
            continue
        else:
            if s+(n-1)*i < end:
                end = s+(n-1)*i
                start = s
                t = i
    return start, end, t
 
t = int(input())
for _ in range(t):
    n,x,y = map(int,input().split(' '))
    start,end,t = solve(n,x,y)
    for i in range(start,end+t,t):
        print(i,end=' ')
    print('')