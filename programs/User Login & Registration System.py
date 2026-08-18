import os

FILE_NAME = "users.txt"

# Create file if it does not exist
if not os.path.exists(FILE_NAME):
    open(FILE_NAME, "w").close()


def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open(FILE_NAME, "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")
            if user == username:
                print("Username already exists!")
                return

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration Successful!")


def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    with open(FILE_NAME, "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")
            if user == username and pwd == password:
                print("Login Successful!")
                return

    print("Invalid Username or Password!")


while True:
    print("\n===== USER LOGIN & REGISTRATION SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
