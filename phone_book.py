

path = "phone_book.txt"
phone_book = []


def get_number(message, error_message):
    control = False
    while control == False:
        test = input(message)
        if test.isdigit() == True:
            result = int(test)
            control = True
        else:
            print(error_message)

    return result

def open_file():
    with open(path, "r", encoding="utf8") as file:
        data = file.readlines()
    for item in data:
        item = item.strip().split(";")
        contact ={"name": item[0],
                  "phone": item[1],
                  "comment": item[2]}
        phone_book.append(contact)

def save_file():
    with open(path, "w", encoding="utf8") as file:
        for contact in phone_book:
            data = ";".join(v for v in contact.values())
            file.write(data + "\n")
def change_contact(book: dict, index: int):
    contact = add_contact()
    return {"name": contact.get("name") if contact.get("name") else book[index - 1].get("name"),
            "phone": contact.get("phone") if contact.get("phone") else book[index - 1].get("phone"),
            "comment": contact.get("comment") if contact.get("comment") else book[index - 1].get("comment")}


def add_contact():
    name = input("enter name: ")
    phone = input("enter phone: ")
    comment = input("enter comment: ")
    return {"name": name, "phone": phone, "comment": comment}

def show_contacts(book, message):
    if not book:
        print(f"******************** {message} *********************")
    else:
        for i, contact in enumerate(book, 1):
            print(f"{i}. {contact.get('name'):<20}"
                  f"{contact.get('phone'):<20}"
                  f"{contact.get('comment'):<20}")

def find_contact():
    if phone_book:
        result = []
        try_string = input("enter information of contact:")
        for contact in phone_book:
            for field in contact.values():
                if try_string.lower() in field.lower():
                    result.append(contact)
        return result
    else:
        print("phonebook empty or not open")
def del_contact():
    if phone_book:
        del_index = get_number("enter number of removable contact:", f"try again it must be digit from 1 to {len(phone_book)}")
        del_element = phone_book.pop(del_index - 1)
        print(f"************************** contact {del_element.get('name')} succesfully deleted ******************************")
    else:
        print("phonebook empty or not open")

menu ="""1.Open phonebook file
2.Save phonebook file
3.Show all contacts
4.Find contact
5.Add contact
6.Change contact
7.Delete contact
8.Exit
"""
while True:
    print(menu)
    choice = get_number("select menu item: ","ENTER NUMBER from 1 to 8")



    match choice:
        case 1:
            open_file()
            print("***********************file opened successfully******************")
        case 2:
            save_file()
            print("*******************************file saved**********************************")
        case 3:
            show_contacts(phone_book, "phone book empty or not open")
        case 4:
            result = find_contact()
            show_contacts(result,"contacts not found")
        case 5:
            new_contact = add_contact()
            phone_book.append(new_contact)
            print("******************* contact sucsesfully added **************************")
        case 6:
            show_contacts(phone_book, "file not open")
            index = get_number("enter number of changing contact: ",f"try again it must be digit from 1 to {len(phone_book)}")
            print("if you don't want to change some fields,leave it empty: ")
            contact = change_contact(phone_book, index)
            phone_book[index-1] = contact
        case 7:
            show_contacts(phone_book,"file not open")
            del_contact()
        case 8:
            print("goodbye")
            break




