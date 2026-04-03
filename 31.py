"""#Create car = {"brand": "Toyota", "model": "Fortuner", "year": 2020} and print only model
car = {"brand": "Toyota", "model": "Fortuner", "year": 2020}
print(car["model"])

#In person = {"name": "Aman", "age": 19}, add key "city" with value "Delhi".

person = {"name": "Aman", "age": 19}

person["city"] =  "Delhi"
print(person)

#In book = {"title": "Python", "price": 500}, update price to 550.

book = {"title": "Python", "price": 500}
book."""


#In user = {"name": "Riya", "email": "riya@mail.com", "phone": "9999"}, remove "phone".

"""user = {"name": "Riya", "email": "riya@mail.com", "phone": "9999"}
user.pop("phone")
print(user)

#Check if key "email" exists in user and print True/False.
book = {"title": "Python", "price": 500}
book["price"] = 550
print(book)
"""
#d = {"a": 1, "b": 2} → make "b" as 20
d = {"a": 1, "b": 2}
d["b"] = 20
print(d)

#d = {"name": "Raj"} → add "age": 19 using update()
d = {"name": "Raj"}
d["age"] = "19"
print(d)

#d1 = {"x": 1}; d2 = {"y": 2} → merge into d1 using update()
d1 = {"x": 1}

d2 = {"y": 2}
d1.update(d2)
print(d1)