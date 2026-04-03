"""Grading system with validation:

Invalid marks (<0 or >100)

A / B / C / Fail"""

marks = int(input("Enter marks : "))


if(marks <0 or marks >100):
    print("Invalid marks")
elif(marks <= 100 and marks >=90):
    print("A")
elif(marks >=80):
    print("B")
elif(marks >= 70):
    print("C")

else: 
    print("Fail")