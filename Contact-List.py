import string

contacts={}

def add_contact() :
    name=input("Enter name : ")
    phone=input("Enter contact number : ")
    contacts[name]=phone
    print("Contact added!")

def delete_contact() :
    name=input("Enter name to delete : ")
    for n in contacts :
       if n==name :
           del contacts[name]
           print("Contact deleted!")
       else :
           print("Contact not found!")

def view_contact() :
    name=input("Enter name to view contact : ")
    if contacts :
      for name , phone in contacts.items() :
        print (f"{name} : {phone}")
    else :
       print("Contact not found!")

def search_contact() :
   name=input("Enter name to search : ")
   if contacts :
      if name in contacts :
         print("Phone number : ",contacts[name])   
   else :
      print("Contact not found!")

while True :
   print("\n1. Add contact")
   print("\n2. Delete contact")
   print("\n3. View Contact")
   print("\n4. Search Contact")
   print("\n5.Exit")

   choice = int(input("Enter choice : "))
   
   if choice == 1 :
      add_contact()
   elif choice == 2 :
      delete_contact()
   elif choice == 3 :
      view_contact()
   elif choice == 4 :
      search_contact()
   elif choice == 5 :
      break
   else :
      print("Invalid choice")