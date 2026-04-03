#Write a program to check whether three sides form a valid triangle.

side1 = int(input("Enter the first side of Triangle : "))
side2 = int(input("Enter the second side of Triangle : "))
side3 = int(input("Enter the third side of Triangle : "))

if(side1+side2+side3 == 180):
    print("valid triangle")
else:
    print("Invalid triangle") 