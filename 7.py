#WAP to find if a number is devisable by 5

num = int(input("Enter the number : "))
num = num%5
if(num == 0):
    print("Number is divisable by 5")
else:
    print("not")
