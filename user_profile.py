class UserProfile:
    def __init__(self, username):
        self.username = username
        self.__isVerified = False  # Private attribute

    def get_verification_status(self):
        return self.__isVerified

    def display_profile(self):
        status = "Verified" if self.__isVerified else "Unverified"
        print(f"Username: {self.username}, Status: {status}")

    def _admin_verify(self):
        self.__isVerified = True
        print(f"Admin verified '{self.username}'.")

    def update_username(self, new_name):
        self.username = new_name
        print(f"Username updated to '{new_name}'.")

# User database
users = {}

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"

def admin_login():
    print("\nADMIN LOGIN")
    username = input("Username: ")
    password = input("Password: ")
    return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

# Main menu loop
while True:
    print("\nUSER VERIFICATION SYSTEM")
    print("1. Add User")
    print("2. View All Profiles")
    print("3. Admin: Verify User")
    print("4. Update Username")
    print("5. Delete User")
    print("6. Exit")

    choice = input("Choose an option (1-6): ").strip()

    if choice == "1":
        name = input("Enter new username: ")
        if name in users:
            print("User already exists.")
        else:
            users[name] = UserProfile(name)
            print(f"User '{name}' added.")

    elif choice == "2":
        print("\nUser Profiles:")
        if not users:
            print("No users found.")
        else:
            for profile in users.values():
                profile.display_profile()

            print("\nEncapsulation Test:")
            for profile in users.values():
                try:
                    print(profile.__isVerified)
                except AttributeError:
                    print(f"{profile.username}: Cannot access __isVerified directly (encapsulation works).")
                print(f"{profile.username} status via method: {profile.get_verification_status()}")

    elif choice == "3":
        if admin_login():
            name = input("Enter username to verify: ")
            if name in users:
                users[name]._admin_verify()
            else:
                print("User not found.")
        else:
            print("Access denied. Invalid admin credentials.")

    elif choice == "4":
        old_name = input("Enter current username: ")
        if old_name in users:
            new_name = input("Enter new username: ")
            if new_name in users:
                print("New username already exists.")
            else:
                users[old_name].update_username(new_name)
                users[new_name] = users.pop(old_name)
        else:
            print("User not found.")

    elif choice == "5":
        name = input("Enter username to delete: ")
        if name in users:
            del users[name]
            print(f"User '{name}' deleted.")
        else:
            print("User not found.")

    elif choice == "6":
        print("Exiting verification system.")
        break

    else:
        print("Invalid choice. Please select from 1 to 6.")