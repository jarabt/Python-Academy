seconds = int(input("Please enter the no. of seconds since midnight: "))

hod = seconds // 3600
min = (seconds % 3600) // 60
if len(str(min)) == 1:
    min = "0" + str(min)

ampm = "AM"
if hod > 12:
    hod -= 12
    ampm = "PM"

print(hod, ":", min, ampm)
