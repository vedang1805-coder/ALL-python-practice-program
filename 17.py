"""Check whether a number is divisible by both 3 and 5, only 3, only 5, or none"""

num = int(input("Enter any number : "))
if(num%3 == 0 and num%5 == 0):
    print("Number is Divisible by 3 and 5")
else:
    print("Number is notDivisible by 3 and 5")