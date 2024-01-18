import math
Radius = int(input("Enter the radius of the circle: "))
print(f"The area of the cirlce with the radius {Radius} is {round(math.pi*Radius*Radius,2)}")
Base = int(input("Enter the base of the triangle: "))
Height = int(input("Enter the height of the triangle: "))
print(f"The area of the triangle with base {Base} and height {Height} is {round(1/2*(Base*Height),2)}")
Length = int(input("Enter the length of the rectangle: "))
Breadth = int(input("Enter the Breadth of the rectangle: "))
print(f"The area of the rectangle is {round(Length*Breadth,2)}")