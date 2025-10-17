

contacts = {} # Create an empty dictionary to hold all the contacts


def add_contact():# This function will let the user add a new contact
    name = input("Enter a name: ")  # Ask for the contact's name
    number = input("Enter a 10-digit phone number: ")  # Ask for the number

   
    if number.isdigit() and len(number) == 10: # Check if the number is only digits and exactly 10 numbers long
        contacts[name] = number  # Add the contact to the dictionary
        print("Contact added!")  # Let the user know it worked
    else:
       
        print("Phone number must be 10 digits and only numbers.") # If it's not a good phone number, tell the user


def delete_contact():# This function will delete a contact from the dictionary
    name = input("Enter the name to delete: ")  # Ask for the name to delete

    
    if name in contacts:# Check if the contact is actually in the dictionary
        del contacts[name]  # Delete the contact
        print("Contact deleted!")  # Confirm it worked
    else:
       
        print("That contact does not exist.") # If the contact doesn't exist, tell the user


def show_contacts():# This function shows all the contacts that are saved
    
    if len(contacts) == 0: # If the dictionary is empty, there are no contacts yet
        print("No contacts yet!")
    else:
       
        print("Your contacts:") # Print each contact's name and number
        for name in contacts:
            print(name + ": " + contacts[name])


#  loop to keep asking the user what they want to do
while True:
    print("\nWhat do you want to do?")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Show Contacts")
    print("4. Quit")

   
    choice = input("Pick 1, 2, 3 or 4: ") # Ask the user to choose what they want to do

    
    if choice == "1":# Depending on the user choice it call the right function
        add_contact()
    elif choice == "2":
        delete_contact()
    elif choice == "3":
        show_contacts()
    elif choice == "4":
        print("Goodbye!")  # End the program
        break  # Exit the loop
    else:
        # If the user types something weird, tell them it's not valid
        print("That is not a valid choice.")
