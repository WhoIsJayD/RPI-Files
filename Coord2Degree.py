from math import sin, cos, atan, acos, sqrt, degrees, radians, pi

def coordinate_to_degrees(x, y):
    x += 0.00001
   
    if x >= 0 and y >= 0:
        angle = degrees(atan(y/x))
    elif x < 0 and y >= 0:
        angle = 180 + degrees(atan(y/x))
    elif x < 0 and y < 0:
        angle = 180 + degrees(atan(y/x))
    elif x >= 0 and y < 0:
        angle = 360 + degrees(atan(y/x))
    return round(angle, 1)

def IK(pos):
    x, y, z = pos[0], pos[1], pos[2]
    x += 0.0000001
   
    coxa = 40
    femur = 40
    tibia = 10
   
    theta1 = coordinate_to_degrees(x, y)
   
    x -= coxa * cos(radians(theta1))
    y -= coxa * sin(radians(theta1))
   
    if theta1 > 180:
        theta1 -= 360
   
    P = sqrt(x**2 + y**2)
   
    if sqrt(x**2 + y**2 + z**2) > femur + tibia:
        print("MATH ERROR: coordinate too far")
        return [theta1, 0, 0]
   
    alpha = atan(z / P)
   
    c = sqrt(P**2 + z**2)
   
    beta = acos((femur**2+c**2-tibia**2) / (2*femur*c))
    theta2 = beta + alpha
    theta3 = acos((tibia**2+femur**2-c**2) / (2*tibia*femur)) - pi
   
    return round(theta1, 1), round(degrees(theta2), 1), round(degrees(theta3), 1)

# Continuously input coordinates from the user
while True:
    try:
        x = float(input("Enter x-coordinate: "))
        y = float(input("Enter y-coordinate: "))
        z = float(input("Enter z-coordinate: "))
        angles = IK([x, y, z])
        print(f"Angles: {angles}")
    except ValueError:
        print("Invalid input. Please enter valid coordinates.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        break
