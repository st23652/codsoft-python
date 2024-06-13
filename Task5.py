class Task5:
    class contact:
        def __init__(self, name, phoneNo, email, address):
            self.name = name
            self.phoneNo = phoneNo
            self.email = email
            self.address = address

    class contactManager:
        def __init__(self):
            self.contacts = []

        def add(self, contact):
            self.contacts.append(contact)

        def view(self):
            for contact in self.contacts:
                print(f"name: {contact.name}, mobile number: {contact.phoneNo}")

        def search(self, keyword):
            found = []
            for contact in self.contacts:
                if keyword.lower() in contact.name.lower() or keyword in contact.phoneNo:
                    found.append(contact)
            return found

        def update(self, name, newPhoneNo, newEmail, newAddress):
            for contact in self.contacts:
                if contact.name == name:
                    contact.phoneNo = newPhoneNo
                    contact.email = newEmail
                    contact.address = newAddress
                    break

        def delete(self, name):
            self.contacts = [contact for contact in self.contacts if contact.name != name]

        def display(self, contact):
            print(f"name: {contact.name}")
            print(f"mobile number: {contact.phoneNo}")
            print(f"email: {contact.email}")
            print(f"address: {contact.address}")

    def interaction(self):
        contactManager = self.contactManager()
        while True:
            print("Menu:")
            print("1: add contact")
            print("2: view contacts")
            print("3: search contacts")
            print("4: update contact")
            print("5: delete contact")
            print("6: exit")

            option = input("enter your option: ")

            if option == '1':
                name = input("enter name: ")
                phoneNo = input("enter mobile number: ")
                email = input("enter email: ")
                address = input("enter address: ")
                contactManager.add(self.contact(name, phoneNo, email, address))
            elif option == '2':
                print("all contacts: ")
                contactManager.view()
            elif option == '3':
                keyword = input("enter keyword to search: ")
                found = contactManager.search(keyword)
                print(f"search results for '{keyword}':")
                for contact in found:
                    contactManager.display(contact)
            elif option == '4':
                name = input("enter name of contact to update: ")
                newPhoneNo = input("enter new phone number: ")
                newEmail = input("enter new email: ")
                newAddress = input("enter new address: ")
                contactManager.update(name, newPhoneNo, newEmail, newAddress)
            elif option == '5':
                name = input("enter name of contact to delete: ")
                contactManager.delete(name)
            elif option == '6':
                print("exiting")
                break
            else:
                print("invalid option, please try again")

if __name__ == "__main__":
    task = Task5()
    task.interaction()
