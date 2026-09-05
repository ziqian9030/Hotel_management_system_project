
def login():
    while True:
        print(" ======= Login =======")
        user_name = input(" Enter admin name : ")
        if user_name == "alan":
            password = int(input(" Enter the password : "))
            if password == 67:
                print(" Login success !")
                return True
            else:
                print(" Wrong password ")
                return False
        else:
            print("Wrong admin name")
            return False