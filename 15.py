"""Take a username and password:

If username is "admin" and password is "1234", print "Login Successful"

Else print "Login Failed"""

uname = str(input("Enter user name : "))
password = int(input("Enter the password : "))

if(uname == "admin" and password == 1234):
    print("Login Successful")
else:
    print("login faild")