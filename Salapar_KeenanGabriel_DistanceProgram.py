import math

point_x1 = float(input("Enter x1: "))
point_x2 = float(input("Enter x2: "))
point_y1 = float(input("Enter y1: "))
point_x1 = float(input("Enter y2: "))

point_x = point_x2 - point_x1
point_y = point_y2 - point_y1

point_xy = pow(point_X, 2) + pow(point_y, 2)

distance = math.sqrt(point_xy)
print("The distance is ", distance)