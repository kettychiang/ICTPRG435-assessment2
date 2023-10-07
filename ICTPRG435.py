# File name: ICTPRG435
# Developer: Ketty Chiang
# Script purpose: Password Manager Script for DigiCore
# Date development began: 2/10/2023
# Date development ended: 5/10/2023

# Create a list of stored credentials
credentials = []

# Create a function to display main menu
def main_menu():
    print("\nAction:")
    print("1. Enter username, password and URL")
    print("2. View stored credentials")
    print("3. Exit")

# Create a function to add a new username and password
def add_credentials():
    username = input("Please enter your username. ")
    password = input("Please enter your password. ")
    url = input("Please enter the URL for the site or resources. ")
    credentials.append({"Username": username, "Password": password, "URL": url})
    print("Information added successfully!")

# Create a function to view stored credentials. 
def view_credentials():
  for i, credential in enumerate(credentials):
    print('\nUser No. %d:' % (i + 1))
    for key, value in credential.items():
      print("%s = %s" % (key, value))

# Main loop
while True:
    main_menu()
    choice = input("Please select your action (1/2/3): ")
    if choice == "1":
        add_credentials()
    elif choice == "2":
        view_credentials()
    elif choice == "3":
        print("Exiting script. Goodbye!")
    else:
        print("Invalid choice. Please select a valid option.")