# Dinner Guest List Generator

# Define a Function to add a person to a list
def add_guest(dinner_list: list, guest: str):
    "Adds a guest to the dinner list"
    dinner_list.append(guest)
    return dinner_list

# Define a Function to remove a person from the list
def remove_guest(dinner_list: list, guest: str):
    "Removes a guest from the dinner list"
    if guest in dinner_list:
        dinner_list.remove(guest)
    # When the person is not in the list
    else:
        print(f"{guest} is not in your list.")
    return dinner_list    


# Define a Function to display the list

def view_list(dinner_list: list):
    "This Displays the current Dinner List"
    if dinner_list:
        print("\n Your Dinner Guest List: ")
        for index, guest in enumerate(dinner_list, start=1):
            print(index, guest)

    # When there is nobody in the list
    else:
        print("You have nobody in your list!")

def print_list(dinner_list: list):
    "This Prints out the Invitations for Each Guest"



# Create list
dinner_list = []

# Ask the user how many guests they want to invite
while True:
    print("Options: (1) Add Guest (2) Remove Guest (3) View Guests Invited (4) Print Out Invitations (5) Exit")
    choice = input("Enter in your choice: ")

    if choice == "1":
        guest = input("Enter in your Guest Name you want to Add: ")
        dinner_list = add_guest(dinner_list, guest)

    elif choice == "2":
        guest = input("Enter in the Guest Name you want to Remove: ")
        dinner_list = remove_guest(dinner_list, guest)
        
    elif choice == "3":
        view_list(dinner_list)

    elif choice == "4":
        print("kkk")
        break

    elif choice == "5":
        pass

    else:
        print("Invalid choice, please enter 1, 2, 3, 4, or 5")

# Create a loop that will keep appending names to the list until the maximum number is reached (6)



# Add names to the list



# Print out invitations for each guest



