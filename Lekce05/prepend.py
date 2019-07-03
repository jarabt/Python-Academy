i_string = input("Please enter a string: ")

if i_string[0:9] == "However, ":
    print(i_string)
else:
    print("However, " + i_string[0].lower() + i_string[1:])
