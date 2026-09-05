def add_guest():
    id = int(input(" Enter ID : "))
    name = input(" Enter name : ")
    age = int(input(" Enter age : "))
    phone_number = int(input(" Enter phone number : "))
    room_number = input(" Enter rooom number : ")
    night = int(input(" Enter number of night stayed in the hotel : "))
    price = int(input(" Enter the price per room : "))

    file = open("guest.txt","a")
    file.write(f" ID : {id}\n")
    file.write(f" name : {name}\n")  
    file.write(f" age : {age}\n")  
    file.write(f" phone_number : {phone_number}\n")  
    file.write(f" room_number : {room_number}\n")  
    file.write(f"Nights : {night}\n")  
    file.write(f"Price per night : {price}\n")  
    file.close()

def show_guest():
    file = open("guest.txt","r")
    data = file.read()
    print(data)
    file.close()

def search_guest():
    search = input(" Enter guest name to search : ")
    file = open("guest.txt","r")
    data = file.read()
    if search in data:
        print(" Guest found !")
    else:
        print(" No guest found !")
    file.close()

def update_guest():
    file = open("guest.txt","r")
    lines = file.readlines()
    update = input(" Enter guest name to update : ")
    found = False
    i = 1

    while i < len(lines):
        line = lines[i]
        if update in line:
            found = True
            new_id = int(input(" Enter new ID : "))
            new_name = input(" Enter new name : ")
            new_age = int(input(" Enter new age : "))
            new_phone = input(" Enter new phone  number : ")
            new_room = int(input(" Enter new room number : "))
            new_night = int(input(" Enter new night staying : "))
            new_price = int(input(" Enter new price : "))
            lines[i-1] = f" ID : {new_id}\n"
            lines[i] = f" Name : {new_name}\n"
            lines[i+1] = f" Age : {new_age}\n"
            lines[i+2] = f" Phone number : {new_phone}\n"
            lines[i+3] = f" Room number : {new_room}\n"
            lines[i+4] = f" Nights : {new_night}\n"
            lines[i+5] = f" Price : {new_price}\n"
            break
        i = i+7
    if found == True:
        file = open("guest.txt","w")
        file.writelines(lines)
        file.close()
        print(" Guest information has been updated!")
    else:
        print(" No gues has been found !")

def delete_guest():
    file = open("guest.txt","r")
    delete = input(" Enter the guest name to delete : ")
    lines = file.readlines()
    file.close()
    new_lines = []
    i = 1
    found = False

    while i < len(lines):
        line = lines[i]
        if delete in line:
            found = True
        else:
            new_lines.append(lines[i-1])
            new_lines.append(lines[i])
            new_lines.append(lines[i+1])
            new_lines.append(lines[i+2])
            new_lines.append(lines[i+3])
            new_lines.append(lines[i+4])
            new_lines.append(lines[i+5])
            new_lines.append(lines[i+6])
            new_lines.append(lines[i+7])
        i = i+7
    if found == True:
        file = open("guest.txt","w")
        file.writelines(new_lines)
        file.close()
        print(" The guest has been deleted !")
    else:
        print(" No guest has been found !")

def exit():
    print(" Thank you")