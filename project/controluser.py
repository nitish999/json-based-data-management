import json
import os

file_name = 'user_record.json'

def load_data():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):
                return [data]
            return data
    return []

def save_data(data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully saved to {file_name}")
#Create a new user record
def create_user():
    user_data = {}
    user_data['id'] = input("Enter your id: ")
    user_data['name'] = input("Enter your name: ")
    user_data['email'] = input("Enter your email: ")
    user_data['age'] = int(input("Enter your age: "))
    return user_data

def save_to_json(user_data):
    data = load_data()
    print(f"Data before adding new user: {data}")  # Debug: Show existing data
    data.append(user_data)
    print(f"Data after adding new user: {data}")  # Debug: Show updated data
    save_data(data)
 
#read user records

def read_users():
        users=load_data()
        if not users:
            print("No user records found.")
            return
        print("Select an option to display users:")
        print("1.Display all users")
        print("2.Retrieve user by ID")
        option=input("Enter your choice:")
        if option=='1':
            for user in users:
                print(user)
        elif option=='2':
            user_id=input("Enter user ID to retrieve:")
            user=next((user for user in users if user['id']==user_id), None)
            if user:
                print(user)
            else:
                print(f"No user found with ID {user_id}")
        else:
            print("Invalid option selected.")

#update user record
def update_user():
    user_id=input("Enter user ID to update:")
    users=load_data()
    user=next((user for user in users if user['id']==user_id),None)
    if not user:
        print(f"No user found with ID {user_id}")
        return
    name=input("Enter new user name :")
    email=input("Enter new user email:")
    age_input=input("Enter new user age:")

    if name:user['name']=name
    if email:user['email']=email
    if age_input:user['age']=int(age_input)
    save_data(users)
    print("User updated successfully.")

#Delete user record
def delete_user():
    user_id=input("Enter user ID to delete: ")
    users=load_data()
    new_users=[user for user in users if user ['id'] != user_id]
    if len(new_users)==len(users):
        print(f"No user found with ID {user_id}")
    else:
        save_data(new_users)
        print("User deleted successfully.")

#console interface for CRUD operations


def main():
    while True:
        print("\nJSON-Based Data Management System")
        print("1. Create User")
        print("2. Read Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            user_data = create_user()
            save_to_json(user_data)
        elif choice == '2':
            read_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()





