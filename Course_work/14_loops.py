email, pwd = 'xyz@gmail.com', '1234'
max_attempts = 5
attempts = 0
while attempts < max_attempts:
    user_email = input("Enter your email: ")
    user_pwd = input("Enter your password: ")
    
    if user_email == email and user_pwd == pwd:
        print("Login successful!")
        break
    else:
        print(f"Invalid credentials, please try again. You have {max_attempts-attempts-1} left.")
    attempts += 1
else:
    print("Maximum attempts reached. Please try after 5 mins.")