import math
def circle_area(R) ->float:
    return(f"The area of the cirlce with the radius {R} is {round(math.pi*R*R,2)}")
Radius = int(input("Enter the radius of the circle: "))
print(circle_area(Radius))
def triangle_area(B, H)-> float:
    return(f"The area of the triangle with base {B} and height {H} is {round(1/2*(B*H),2)}")
Base = int(input("Enter the base of the triangle: "))
Height = int(input("Enter the height of the triangle: "))
print(triangle_area(Base, Height))
def rectangle_area(L, B)-> float:
    return(f"The area of the rectangle is {round(L*B,2)}")
Length = int(input("Enter the length of the rectangle: "))
Breadth = int(input("Enter the Breadth of the rectangle: "))
print(rectangle_area(Length,Breadth))
def square_perimeter(Side)-> float:
    return(f"The perimter of the square is {4*Side}")
print(square_perimeter(5))
def circle_details(Radius)-> float:
    print(f"The area of the circle is {circle_area(Radius)} and the circumfrence of the circle is {2*math.pi*Radius}")
def geometry(Square_Side, Circle_Radius):
    if square_perimeter(Square_Side)>2*math.pi*Circle_Radius:
        print("The square has a largetr perimter than the circumfrence of the circle")
    elif 2*math.pi*Circle_Radius>square_perimeter(Square_Side):
        print("The circle has a largetr circumfrence than the perimeter of the square")
    else:
        print("The square perimter and the circle circumfrence are the same size")
    if rectangle_area(Square_Side,Square_Side)>circle_area(Circle_Radius):
        print("The area of the square is greater")
    elif circle_area(Circle_Radius)>rectangle_area(Square_Side,Square_Side):
        print("The area of the circle is greater")
    else:
        print("The area of the circle and the square are the same")