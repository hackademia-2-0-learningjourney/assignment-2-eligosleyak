import json

def register_user(file_name):
    attempt_count = 1
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    confirm_password = input("Confirm password: ")
    
    while user_password != confirm_password and attempt_count != 3:
        print("Password mismatch")
        user_password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        attempt_count += 1
        
    if attempt_count >= 3 and user_password != confirm_password:
        print("Too many wrong attempts. Registration failed.")
    else:
        user_mobile = input("Enter mobile number: ")
        user_details = {
            user_name: {
                'password': user_password,
                'mobile': user_mobile
            }
        }
        
        try:
            try:
                with open(file_name, 'r') as file:
                    users_data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                users_data = {}
                
            users_data.update(user_details)
            with open(file_name, 'w') as file:
                json.dump(users_data, file, indent=4)

            print("Registration successful!")
        except Exception as error:
            print(f"An error occurred: {error}")

def login_user(file_name):
    user_name = input("Enter username: ")
    user_password = input("Enter password: ")
    
    try:     
        with open(file_name) as file:
            users_data = json.load(file)
    except Exception as error:
        print(error)
        return
        
    if user_name in users_data and users_data[user_name]['password'] == user_password:
        print(f"Welcome {user_name}!")
        print(f"Mobile number: {users_data[user_name]['mobile']}")
    else:
        print("Incorrect credentials. Access denied.")

def main():
    file_name = "user_data.json"
    print("1. Log In\n2. Register\n3. Exit")
    user_choice = int(input("Enter your choice: "))
    
    if user_choice == 1:
        login_user(file_name)
    elif user_choice == 2:
        register_user(file_name)
    elif user_choice == 3:
        print("Exiting...")
    else:
        print("Invalid choice, please try again.")
        main()

if __name__ == "__main__":
    main()
