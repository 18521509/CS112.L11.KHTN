from math import pi, pow
def solve(v):
    return 6*pi*pow(v**2/(4.0*pi**2),1.0/3.0)

t = int(input())
res = []
for i in range(t):
    v = float(input())
    res.append(solve(v))

for x in res:
    print(f'{x:.6f}')
