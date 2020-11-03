
A = [0]*40
F = [0]*40
F[0] = 2
A[1] = 9
F[1] = 11
for i in range(2,36):
    k = int('9' + '0'*int((i-1)/2))
    A[i] = A[i-1]+k
    F[i] = 2
    F[i]+= A[i] + F[i-1]
# for i in range(36):
#     print(f'{i} : {F[i]}')

inp = []
t = int(input())
for i in range(t):
    inp.append(int(input()))
for i in inp:
    print(F[i])
