#WWAP to fnd a year is leap year or not
year = int(input("Enter the year : "))
year = year%4
if(year == 0):
    print("Leapyear")
else:
    print("Not leapyear") 