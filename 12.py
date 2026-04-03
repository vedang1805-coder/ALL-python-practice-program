"""11. Take marks as input and print grade:
• ≥ 90 → A
• ≥ 75 → B
• ≥ 60 → C
• < 60 → Fail"""

marks  = int(input("Enter marks : "))

if(marks >= 90):
    print("A")
elif(marks >= 75):
    print("B")
elif(marks >= 60):
    print("C")
else:
    print("Fail")