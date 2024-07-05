import string

print("Input your desired password:")
print(" Ensure that ir has at least one lowercase, one uppercase, one number, one character and it should be between 8-16 characters long.")

passwrd = input()

def valid_passwrd(passwrd):
    if not any (char in string.ascii_lowercase for char in passwrd):
        print("Missing lower case(a-z).")
        return False
    if not any (char in string.ascii_uppercase for char in passwrd):
        print("Missing uppercase (A-Z).")
        return False
    if not any (char in string.digits for char in passwrd):
        print("Missing numbers (0-9).")
        return False
    if not any (char in string.punctuation for char in passwrd):
        print("Missing special symbols(#,$,&...).")
        return False
    if len(passwrd) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if len(passwrd) > 16:
        print("Password must not be longer than 16 characters.")
        return False
    return True    

if valid_passwrd(passwrd):
    print("Password is valid!")
else:
    print("Password is invalid")
    