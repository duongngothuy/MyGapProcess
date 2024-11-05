import json

class Contact:
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number 
        self.email = email
        self.address = address
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.number}, Email: {self.email}, Address: {self.address}"
    def to_dict(self):
        return {"name": self.name, "phone": self.number, "email": self.email, "address": self.address}

Contacts_list = []

def Add_Contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    new_contact = Contact(name, number, email, address) #creating new object to add to contacts
    Contacts_list.append(new_contact)
    print("Contact added successfully")

def View_All_Contacts():
    for i in Contacts_list:                    
        if i not in Contacts_list:
            print("No contacts are found. Please try again")
            return #exit immediately after the for loop, no need to else condition
    print("Your contacts: ")
    for index, each in enumerate(Contacts_list, start = 1):
        print(f"{index}. {each}") #coi lai dong nay

def Search_For_Contacts():
    search_name = input("Enter the contact you are searching: ")
    for i in Contacts_list:
        if i.name.lower() == search_name.lower():
            print("Contact found")
            print(i)
            break
        else:
            print("No contacts found. Please try again with a different name")

def Edit_Contacts():
    edit_name = input("Enter the contact to edit: ")
    for i in Contacts_list:
        if i.name.lower() == edit_name.lower():
            print("Editing the contact", i)

            name = input("Enter to update name, leave as blank to keep original") or i.name
            number = input("Enter to update number, leave as blank to keep original") or i.number 
            email = input("Enter to update email, leave as blank to keep original") or i.email
            address = input("Enter to update address, leave as blank to keep original") or i.address

        i.name = name 
        i.number = number 
        i.email = email
        i.address = address 
        print("The contact is updated successfully!")
        return
    print("No contacts found to update")

def Delete_Contacts():
    delete_name = input("Enter the name to delete: ")
    for i in Contacts_list:
        if i.name.lower() == search_name.lower():
            confirm_option = input("Are you sure you want to delete the contact? (y/n) ")
            if confirm_option == 'y':
                Contacts_list.remove(i)
                print("The contact is successfully deleted")
            else:
                print("Deletion is cancelled")
            return
    print("No contacts found to delete")



def Save_Contacts_toFile():
    for i in Contacts_list:
        contact_dict = i.to_dict()
    
    with open("contacts.json", "w") as file:
        json.dump(contact_dict, file, indent=4) #easier to read with indent 4

    print("Contacts saved to 'contacts.json' successfully!")

def load_contacts_from_file():
    try:
        # Open the file and load data
        with open("contacts.json", "r") as file:
            contacts_data = json.load(file)

        # Clear existing contacts and load new ones
        Contacts_list.clear()

        for i in contacts_data:
            contact = Contact(
                name=i["name"],
                phone=i["phone"],
                email=i["email"],
                address=i["address"]
            )
            Contacts_list.append(contact)

        print("Contacts loaded successfully!")

    except FileNotFoundError:
        print("No saved contacts found. Starting with an empty address book.")
    except json.JSONDecodeError:
        print("Error loading contacts. The file might be corrupted.")

def exit_program():
    answer = input("Would you like to save your contacts before exiting? (y/n): ").strip().lower() #strip is for handling extra spaces from the answer
    if answer == 'y':
        Save_Contacts_toFile()
        print("Thank you for using the Address Book!")
    exit()  

def main_menu():
    while True:
        print("Welcome to your Address Book!")
        print("1. Add a contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Edit a contact")
        print("5. Delete a contact")
        print("6. Save contacts to file")
        print("7. Load contacts from file")
        print("8. Exit")

        try:
            different_choices = int(input("Enter your choice: "))
        except ValueError:
            print("Input must be a number. Please try again!")
            continue

        match different_choices: 
            case 1:
                Add_Contact()
            case 2:
                View_All_Contacts()
            case 3:
                Search_For_Contacts()
            case 4:
                Edit_Contacts()
            case 5:
                Delete_Contacts()
            case 6:
                Save_Contacts_toFile()
            case 7:
                Load_Contacts_fromFile()
            case 8:
                print("Thank you for using the Address Book!")
                break 
            case _:
                print("Invalid choice. Please select a valid option.")
    # except ValueError:
    #     print("Input must be a number. Please try again!")
        # continue


if __name__ == "__main__": #run the main menu
    main_menu()
    
    


    
    






        

    




