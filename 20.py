"""If units are 100 or less → charge ₹1 per unit

If units are between 101 and 200 → charge ₹2 per unit

If units are more than 200 → charge ₹3 per unit"""

units = int(input("Enter units : "))

if(units == 0):
    print("Invalid units")
elif(units <=100):
    bill = units*1
    print(" Bill  = ",bill)
elif(units>=101 and units<=200):
    bill = units*2
    print("Bill : ",bill)
elif(units>200):
    bill = units*3
    print("Bill = ",bill)
else:
    print("None") 