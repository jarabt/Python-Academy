anum = input("Please give me a number: ")
if not anum:
    print("No input provided")
else:
    l = len(anum)
    boarder = l//2
    anum1 = anum[:boarder]
    anum2 = anum[boarder:]
    print(anum1 + " " + anum2)
    #conversion to integers
    num1 = int(anum1)
    num2 = int(anum2)
    #conditions
    if not num1%2 and not num2%2:
        print("Success")
    elif not num1%2:
        print("First")
    elif not num2%2:
        print("Second")
    else:
        print("Niether")
