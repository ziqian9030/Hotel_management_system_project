def add_room():
    room = int(input(" Enter room number: "))
    ava = input(" Enter room availability (yes/no): ")
    file = open("room.txt","a")
    file.write(f" Room number: {room}\n")
    file.write(f" Availability: {ava}\n")
    file.close()

def show_room():
    file = open("room.txt","r")
    data = file.read()
    print(data)
    file.close()

def search_room():
    file = open("room.txt","r")
    data = file.read()
    search = input("Enter room number to search: ")
    if search in data:
        print("This room has been found !")
    else:
        print("No room has been found! ")
    file.close()

def update_room():
    update = input(" Enter room to update: ")

    file = open("room.txt","r")
    lines = file.readlines()
    file.close()
    i = 0
    found = False

    while i < len(lines):
        line = lines[i]
        if update in line:
            new_room = int(input(" Enter new room: "))
            new_ava = input("Enter room availability (yes/no): ")
            lines[i] = f"Room: {new_room}\n"
            lines[i+1] = f"availability : {new_ava}\n "
            found = True
            break
        i = i+2
    if found == True:
        file = open("room.txt","w")
        file.writelines(lines)
        file.close()
        print(" The room has been updated !")
    else:
        print(" No room has been found !")

def delete_room():
    file = open("room.txt","r")
    delete = input(" Enter room number to delete: ")
    lines = file.readlines()
    file.close()
    i = 0
    found = False
    new_lines = []

    while i < len(lines):
        line = lines[i]
        if delete in line:
            found = True
        else:
            new_lines.append(lines[i])
            new_lines.append(lines[i+1])
        i = i+2
    if found == True:
        file = open("room.txt","w")
        file.writelines(new_lines)
        file.close()
        print(" The room has been deleted !")
    else:
        print(" No room has been found!")

def exist():
    print(" Thank you ")
