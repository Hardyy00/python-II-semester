import math

a = float(input("Enter the side a : "))
b = float(input("Enter the side b : "))
c = float(input("Enter the side c : "))

angle_a = math.acos((b*b + c*c -a*a)/(2*b*c))
angle_b = math.acos((a*a + c*c - b*b)/(2*a*c))
angle_c = math.acos((a*a + b*b - c*c)/(2*a*b))

print(f"Angle A = {math.ceil(math.degrees(angle_a))}")
print("Angle B =",math.ceil(math.degrees(angle_b)))
print("Angle C =",math.ceil(math.degrees(angle_c)))