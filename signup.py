name = (input("Enter Name :"))
email = (input("Enter email :"))
password = (input("Enter Password :"))
user_details = (any([name, email, password]))
if email.endswith("@gmail.com") and len(password) >= 7:
    print("Registration successful")
else:
    print("Registration failed")
