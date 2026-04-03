#WAP to enter marks of 3 subjects from the user and store them in a dictionary, start with an empty dictionary & add one by one 
dic = {}
x = int(input("Enter phy : "))
dic.update({"phy" : x})
y = int(input("enter che : "))
dic.update({"che" : 34})
z = int(input("Enter bio : "))
dic.update({"bio" : 44})
print(dic)