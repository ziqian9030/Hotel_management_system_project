import function.vip_guests as vip_fuction
import Auth.login as login_fuction
import function.normal_guest as guest_function
if login_fuction.login():
    while True:
        print(" ======= Welcome to hotel system =======")
        print(" 1. Guest management  ")
        print(" 2. Room management  ")
        choice = int(input(" Enter you choice "))
        match choice:
            case 1:
                print(" 1. VIP guest ")
                print(" 2. Normal guest ")
                choice_2 = int(input(" Enter your choice : "))
                match choice_2:
                    case 1:
                        print(" 1. Add VIP ")
                        print(" 2. Show VIP ")
                        print(" 3. Search VIP ")
                        print(" 4. Update VIP ")
                        print(" 5. Delete VIP ")
                        print(" 6. Exit ")
                        choice_3 = int(input(" Enter your choice : "))
                        match choice_3:
                            case 1:
                                vip_fuction.add_vip()
                            case 2:
                                vip_fuction.show_vip()
                            case 3:
                                vip_fuction.search_vip()
                            case 4:
                                vip_fuction.update_vip()
                            case 5:
                                vip_fuction.delete_vip()
                            case 6:
                                vip_fuction.exit()
                                break
                    case 2:
                        print(" 1. Add guest ")
                        print(" 2. Show guest ")
                        print(" 3. Search guest ")
                        print(" 4. Update guest ")
                        print(" 5. Delete guest ")
                        print(" 6. Exit ")
                        choice_4 = int(input(" Enter your choice : "))
                        match choice_4:
                            case 1:
                                guest_function.add_guest()
                            case 2:
                                guest_function.show_guest()
                            case 3:
                                guest_function.search_guest()
                            case 4:
                                guest_function.update_guest()
                            case 5:
                                guest_function.delete_guest()
                            case 6:
                                guest_function.exit()
                                break

                        

