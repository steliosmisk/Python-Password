import secrets
import string

print("--WELCOME TO MY PASSWORD GENERATOR--")
print("[1] Start")
print("[2] Exit")


password_letters = string.ascii_letters + string.digits + string.punctuation
password = ""

user_choice = input("Enter your choice: ")
while user_choice == "1":
    try:
        user_pass_length = int(input("Enter your password length: "))
        for _ in range(user_pass_length):
            password += "".join(secrets.choice(password_letters))
        print("Your Password is:", password)
        break
    except ValueError:
        print("Error! Enter the length not a poem jk.")
