f24 = input("Please enter your time: ")
hod = int(f24.split(":")[0])
ampm = "AM"
if hod > 12:
    hod -= 12
    ampm = "PM"

print(hod, ":", int(f24.split(":")[1]), ampm)
