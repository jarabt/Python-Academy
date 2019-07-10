def gcd(int1, int2):
    rem = int1%int2
    while rem != 0:
        int1 = int2
        int2 = rem
        rem = int1%int2
    return int2







print(gcd(414 , 49))
