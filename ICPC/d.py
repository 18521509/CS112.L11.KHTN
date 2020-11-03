def solve(n):
    i = 0
    if n%7 ==0:
        return n

    while i<1000:
        i+=1
        n += int(str(n)[::-1])
        if n%7 == 0:
            return n
    return -1

t = int(input())
inp = [0]*t
for i in range(t):
    inp[i] = int(input())
for i in inp:
    print(solve(i))
