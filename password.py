import secrets
import string

print("---- WELCOME TO MY PASSWORD GENERATOR ----")
print("[1] Generate Password")
print("[2] Exit")

password_letters = string.ascii_letters + string.digits + string.punctuation

while True:
    user_choice = input("Enter your choice (1/2): ")
    if user_choice == "1":
        try:
            user_pass_length = int(input("Enter the length of your password: "))
            password = "".join(secrets.choice(password_letters) for _ in range(user_pass_length))
            print("Your Password is:", password)
        except ValueError:
            print("Invalid input! Please enter a valid password length.")
    elif user_choice == "2":
        break

    else:
        print("Invalid choice! Please enter a valid choice (1/2).")
