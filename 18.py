"""Write a program to simulate traffic light:

Red → Stop

Yellow → Ready

Green → Go"""

light = str(input("Enter the color of light : "))

if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Ready")
elif(light == "green"):
    print("Go")
else:
    print("Invalid color") 