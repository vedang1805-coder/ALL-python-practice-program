"""Question 15 (Calculator) you are supposed to perform all basic operators.

That means:

+ → Addition

- → Subtraction

* → Multiplication

/ → Division"""

num1  = int(input("Enter the first  number : "))
num2  = int(input("Enter the second  number : "))
op = input("Enter any operator")

if(op == "+"):
    print("Num1 + num2 =  ",num1+num2)
elif(op=="-"):   
    print("num1 - num2 = ",num1-num2)
elif(op=="/"):
    print("num1/num2 = ",num1/num2)
else:
    print("Invalid operator")