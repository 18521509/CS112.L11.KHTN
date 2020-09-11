n = int(input())
A = list(map(int,input().split(',')))

A.insert(0,0)
S = [0] * (n+1)
S[0] = A[0]

for i in range(1,n+1):
    S[i] = A[i]+S[i-1]

pre_min = [0] * (n+1)

for i in range(1,n+1):
    if S[i] < S[pre_min[i-1]]:
        pre_min[i] = i
    else:
        pre_min[i] = pre_min[i-1]

max_sum = S[1]
p,q=1,1

for i in range(2,n+1):
    if S[i] - S[pre_min[i-1]] > max_sum:
        max_sum = S[i] - S[pre_min[i-1]]
        p,q = pre_min[i-1]+1, i

print(p,q,max_sum)
