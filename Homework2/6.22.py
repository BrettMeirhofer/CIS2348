x1 = int(input())
y1 = int(input())
c1 = int(input())
x2 = int(input())
y2 = int(input())
c2 = int(input())
Success = False
for X in range(-10,11):
    for Y in range(-10, 11):
        if((x1*X)+(y1*Y) == c1) and ((x2*X)+(y2*Y) == c2):
            print(X, Y)
            Success = True
            break

    if(Success):
        break

if(Success == False):
    print("No solution")