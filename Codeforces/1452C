n = int(input())
for i in range(n):
    a = input()
    b, c =0,0
    for char in a:
        if char == ']':
            if b > 0:
                b-=1
                c+=1
        elif char == '[':
            b+=1
    b = 0
    for char in a:
        if char == ')':
            if b > 0:
                b-=1
                c+=1
        elif char == '(':
            b+=1
            
    print(c)
