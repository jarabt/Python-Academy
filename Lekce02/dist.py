import math

ax = int(input('Point A, X Coordinate: '))
ay = int(input('Point A, Y Coordinate: '))
bx = int(input('Point B, X Coordinate: '))
by = int(input('Point B, Y Coordinate: '))

dif_x = abs(bx - ax)
dif_y = abs(by - ay)

dist = math.sqrt(pow(dif_x, 2) + pow(dif_y, 2))
dist = round(dist, 2)

print('The distance between the points A and B is ' + str(dist))
