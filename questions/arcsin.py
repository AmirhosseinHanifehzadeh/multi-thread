from math import pi, sin


def Arcsinus(x):
    highDomain = pi / 2
    lowDomain = -1 * pi / 2

    def inner(e): # e is accuracy of returned value
        nonlocal lowDomain
        nonlocal highDomain

        while highDomain - lowDomain >= e:
            mid = (highDomain + lowDomain) / 2

            if sin(mid) <= x:
                lowDomain = mid

            elif sin(mid) > x:
                highDomain = mid

        return round(mid, 4)

    return inner

e, x = input().split()
e = float(e)
x = float(x)
Arcsin_e = Arcsinus(x)
print(Arcsin_e(e))
