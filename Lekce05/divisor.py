start = int(input("start (incl.): "))
stop = int(input("stop (incl.): "))
divisor = int(input("divisor: "))

if divisor == 0:
    print("Cannot divide by zero.")

else:
    result = []

    for n in range(start,stop+1):
        if not n%divisor:
            result.append(n)

    print(result)
