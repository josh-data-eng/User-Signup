name = input("Enter Name: ")
email = input("Enter Email: ")
password = input("Enter Password: ")
fields_filled = all([name, email, password]) 
if fields_filled and email.endswith("@gmail.com") and len(password) >= 7:
    print("Registration successful")
else:
    print("Registration failed")