# Dinner Guest List

# Define a Function to add a person to a list
def add_jovan(dinner_list, human):
    dinner_list.append(human)
    return dinner_list

# Define a Function to remove a person from the list
def remove_jovan(dinner_list, human):
    if human in dinner_list:
        dinner_list.remove(human)
    else:
        print(f"{human} is not in your list.")
    return dinner_list    


# Define a Function to display the list

def display(dinner_list):
    if dinner_list:
        print(dinner_list)
    else:
        print("veiny ah")


# Create list
dinner_list = []

# Ask the user how many guests they want to invite
while True:
    print("Options: (1) Add Guest (2) Remove Guest (3) View Guests Invited (4) Exit")
    choice = input("Enter in your choice: ")

    if choice 

# Create a loop that will keep appending names to the list until the maximum number is reached (6)



# Add names to the list



# Print out invitations for each guest



