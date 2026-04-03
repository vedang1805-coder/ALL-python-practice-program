#WAP to check a character if it is vowel or consnant

char = str(input("Enter the character : "))
char = char.lower()

if(char == "a" or char == "i" or char == "o" or char == "e" or char == "u"):
    print("The character os vowel")
else:
    print("The character is constant") 