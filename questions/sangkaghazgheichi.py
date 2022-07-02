P, R, S, a, b, c = list(map(int, input().split()))
result = 0
value1 = True
value2 = True
value3 = True

# do something to P to become 0
P_diffrent = P - c
if P_diffrent <= 0:
    result += P
    c -= P
    P = 0
else:
    c = 0
    if P - a <= 0:
        a -= P
        P = 0
    else:
        for i in range(1, a + 1):
            P1 = P - i
            if P1 <= 0:
                a = a - i
                P = 0
                value1 = False
                break
        if value1:
            a = 0
            b = b - P1
            result -= P1
            P = 0
# do something with R to become 0
R_diffrent = R - a
if R_diffrent <= 0:
    result += R
    a -= R
    R = 0
else:
    a = 0
    if R - b <= 0:
        b -= R
        R = 0
    else:
        for i in range(1, b + 1):
            R1 = R - i
            if R1 <= 0:
                b = b - i
                R = 0
                value2 = False
                break
        if value2:
            b = 0
            c = c - R1
            result -= R1
            R = 0

# do something to S to become 0
S_diffrent = S - b
if S_diffrent <= 0:
    result += S
    b -= S
    S = 0
else:
    b = 0
    if S - c <= 0:
        c -= S
        S = 0
    else:
        for i in range(1, c + 1):
            S1 = S - i
            if S1 <= 0:
                c = c - i
                S = 0
                value3 = False
                break
        if value3:
            c = 0
            a = a - S1
            result -= S1
            R = 0
print(result)
