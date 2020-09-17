
def solve(a,b,x,y,n):
    if a < b:
        a,b,x,y = b,a,y,x
    p = a-x
    q = b-y
 
    if n >= p+q:
        return x*y
    
    if q >=n: 
        return (a*(b-n))
    
    
    z = p+q - n
    s1 = y*(a+z-p)
    if p >= n:
        s2 = (a-n)*b
    else :
        s2 = x*(b+z-q)
    return min([s1,s2])
        
 
 
 
t = int(input())
for i in range(t):
    a,b,x,y,n = map(int,input().split(' '))
    print(solve(a,b,x,y,n))