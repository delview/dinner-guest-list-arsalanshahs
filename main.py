# Dinner Guest List Generator

# Greet
print("Welcome to the dinner guest list!")

# Create an Invitation Message
invitation = input("Enter in your invitation message (Without the Name) (Ex: You have been invited to dinner): ")


# Define a Function to add a person to a list
def add_guest(dinner_list: list, guest: str, max_guests: int):
    """Adds a guest to the dinner list if there is space"""
    if len(dinner_list) < max_guests:
        dinner_list.append(guest)
        print(f"{guest} has been added to your guest list")
    else:
        print("You have reached the maximum number of guests.")
    return dinner_list

# Define a Function to remove a person from the list
def remove_guest(dinner_list: list, guest: str):
    """Removes a guest from the dinner list only if they exist"""
    if guest in dinner_list:
        dinner_list.remove(guest)
    # When the person is not in the list
    else:
        print(f"{guest} is not in your list.")
    return dinner_list    


# Define a Function to display the list

def view_list(dinner_list: list):
    """This Displays the current Dinner List"""
    if dinner_list:
        print("\n Your Dinner Guest List: ")
        for index, guest in enumerate(dinner_list, start=1):
            print(f"{index}. {guest}")

    # When there is nobody in the list
    else:
        print("You have nobody in your list!")

def print_invitations(dinner_list: list, invitation: str, dinner_time: str):
    """This Prints out the Invitations for Each Guest"""
    if not dinner_list:
        print("You have no guests to invite.")
        return
    
    print("\nInvitation Messages: ")
    for guest in dinner_list:
        print(f"Dear {guest}, {invitation} at {dinner_time}.")

# The Function to set and adjust the dinner time

def set_dinner_time():
    """This Asks the user for the dinner time and also allows them to change it."""
    time = input("Enter the dinner time (e.g., 7:00PM): ").strip()
    while True:
        change = input(f"The current dinner time is {time}. Do you want to adjust it? (yes/no): ")
        if change == "yes":
            time = input("Enter the new dinner time: ")
        
        elif change == "no":
            print("Okay.")
            break
        else:
            ("This is an Invalid input. Please enter a yes or no.")
    return time



# Create list
dinner_list = []

while True:
    try:
        # Ask for number of guests
        max_guests = int(input("Enter in the amount of guests you are inviting: ").strip())
        if max_guests < 1:
            print("There should be at least 1 guest...")
        elif max_guests > 100:
            print("what the-")
            break
        else: 
            break
    except ValueError:
        print("This is an invalid input. Please enter a number.")

# Variable to set the dinner time
dinner_time = set_dinner_time()

# Ask the user how many guests they want to invite
while True:
    print("Options: (1) Add Guests (2) Remove Guest (3) View Guests Invited (4) Print Out Invitations (5) Exit")
    choice = input("Enter in your choice: ")
 
    # Add names to the list only if the max amount of guests isn't full
    if choice == "1":
        while len(dinner_list) < max_guests:
            guest = input("Enter in the name of the guest to add: ").strip()
            dinner_list = add_guest(dinner_list, guest, max_guests)
        if len(dinner_list) == max_guests:
            print("The guest list is full.")
            

    elif choice == "2":
        guest = input("Enter in the Guest Name you want to Remove: ")
        dinner_list = remove_guest(dinner_list, guest)
        
    elif choice == "3":
        view_list(dinner_list)

    # Print out invitations for each guest
    elif choice == "4":
        print_invitations(dinner_list, invitation, dinner_time)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1, 2, 3, 4, or 5")









