def add_vip():
    id = int(input(" Enter VIP ID : "))
    name = input(" Enter VIP name : ")
    age = int(input(" Enter VIP age : "))
    phone_number = int(input(" Enter VIP phone number : "))
    room_number = input(" Enter VIP rooom number : ")
    night = int(input(" Enter number of night stayed in the hotel : "))
    price = int(input(" Enter the price per room : "))

    file = open("vipguest.txt","a")

    file.write(f"VIP ID : {id}\n")
    file.write(f"VIP name : {name}\n")  
    file.write(f"VIP age : {age}\n")  
    file.write(f"VIP phone_number : {phone_number}\n")  
    file.write(f"VIP room_number : {room_number}\n")  
    file.write(f"Nights : {night}\n")  
    file.write(f"Price per night : {price}\n")  
    
    file.close()

def show_vip():
    file = open("vipguest.txt","r")
    data = file.read()
    print(data)
    file.close()

def search_vip():
    sear_vip =input(" Enter vip's ID to search : ")
    file = open("vipguest.txt","r")
    data = file.read()
    if sear_vip in data:
        print(" VIP has been found!")
    else:
        print(" No VIP has been found ")
    file.close()

def update_vip():
    update = input(" Enter VIP name to update : ")
    file = open("vipguest.txt","r")
    lines = file.readlines()
    file.close()
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
        i = i + 7
    if found == True:
        file = open("vipguest.txt","w")
        file.writelines(lines)
        file.close()
        print(" VIP information has been updated !")
    else:
        print(" NO VIP has been found !")

def delete_vip():
    file = open("vipguest.txt","r")
    delt_vip = input(" Enter VIP name to delete : ")
    lines = file.readlines()
    file.close()
    found = False
    new_lines = []
    i = 1

    while i < len(lines):
        line = lines[i]
        if delt_vip in line:
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
        i = i + 7
    if found == True:
        file = open("vipguest.txt","w")
        file.writelines(new_lines)
        file.close()
        print(" The VIP has been deleted !")
    else:
        print(" No vip has been found !")

def exit():
        print(" Thank you ")