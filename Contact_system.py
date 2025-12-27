import json
Contact_data={}



def save_to_file():
    with open("contact_book.json","w") as f:
        json.dump(Contact_data,f,indent=4)



def Add_contact():
    contact_to_add=int(input("Enter the no. of contact to add="))
    for i in range(contact_to_add):
        data2={}
        Name=input("Enter name of contact=").strip().capitalize()
        if Name in Contact_data:
            print("Contact Already Exists!")
            Ask=input("Are you sure you want to overwrite it?\n"
                      "A: Yes\n"
                      "B: No\n"
                      "Enter=").upper()
            if Ask=="A":
                pass
            elif Ask=="B":
                continue
        Mobile_Number=input("Enter mobile number=")
        Email_id=input("Enter the email id=")
        data2["Contact_Number"]=Mobile_Number
        data2["Email_id"]=Email_id
        Contact_data[Name]=data2
    save_to_file()



def Find_contact():
    info=input("What do you want to find?\n"
               "A: Get whole Contact Book\n"
               "B: Find a Contact\n"
               "Enter the choice=").upper()
    if info=="A":
        print(f"{'Name':<12}{'Phone':<15}{'Email Id'}")
        print("-"*45)
        for name,info in Contact_data.items():
            Phone=info["Contact_Number"]
            Email=info["Email_id"]
            print(f"{name:<12}{Phone:<15}{Email}")
    elif info=="B":
        Name=input("Enter the contact name=").strip().capitalize()
        contactname=Contact_data.get(Name)
        if contactname is not None:
            Phone=contactname["Contact_Number"]
            Email=contactname["Email_id"]
            print(f"{Name:<12}{Phone:<15}{Email}")
        else:
            print("Contact not Found!")
        


def Edit_contact():
    Name=input("Enter the contact name=").strip().capitalize()
    if Name in Contact_data:
        print(Contact_data.get(Name))
        Edit=input("What you want to edit?\n" 
                   "A: Contact Number\n"
                   "B: Email Id\n"
                   "C: Both\n"
                   "Enter the option to choose=").upper()
        data2=Contact_data.get(Name)
        if Edit=="A":
            Num=input("Enter the new Contact number=")
            data2["Contact_Number"]=Num
        elif Edit=="B":
            Id=input("Enter the new Email Id=")
            data2["Email_id"]=Id
        elif Edit=="C":
            Num=input("Enter the new Contact number=")
            Id=input("Enter the new Email Id=")
            data2["Contact_Number"]=Num
            data2["Email_id"]=Id
    else:
        print("Contact not found!")
    save_to_file()



def Delete_Contact():
    Name=input("Enter the contact name to delete=").strip().capitalize()
    if Name in Contact_data:
        Contact_data.pop(Name)
    elif Name not in Contact_data:
        print("Contact not found!")
    save_to_file()


def menu():
    global Contact_data
    try:
        with open ("contact_book.json","r") as f:
            Contact_data=json.load(f)
    except FileNotFoundError:
        with open("contact_book.json","w")as f:
            Contact_data={}

    while True:   
        user=input("What you want to do?\n"
                "A: Add contact\n"
                "B: Find contact\n"
                "c: Edit contact\n"
                "D: Delete contact\n"
                "E: Exit\n"
                "Enter the option you want to choose=" ).upper()
        if user=="A":
            Add_contact()
        elif user=="B":
            Find_contact()
        elif user=="C":
            Edit_contact()
        elif user=="D":
            Delete_Contact()
        elif user=="E":
            break
    


menu()
