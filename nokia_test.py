def  phone_book():
    while True:
        print("Phone book(Menu 1)")
        print("In this menu, you can manage the names and phone numbers in the phone and the SIM card.")
        print("1. Search")
        print("2. Service Nos")
        print("3. Add name")
        print("4. Erase")
        print("5. Edit")
        print("6. Copy")
        print("7. Assign Tone")
        print("8. Send b'card")
        print("9.Options - Memory in use")
        print("10. Options - Type of view")
        print("11.Options - Memory status")
        print("12. Speed dials")
        print("13. Voice Tags")
        print("14. Back to Main Menu...")
        phonebook = input("Select an option: ")
        match phonebook:
            case "1":
                print("Search: You can recall the desired name and phone number from the phone book to make a call. When you browse through the names and phone numbers, an indicator is shown in the top right corner of the display if the selected name or phone number is saved in the SIM card ")
            case "2":
                print("Service Nos: Calls the service number of your service provider, which is saved in your SIM card.")
            case "3":
                print("Add name: You can save a name and phone number in the phone book.")
            case "4":
                print("Erase: You can delete names and phone numbers from the selected phone book one by one or all at once.")
            case "5":
                print("Edit: You can modify the names and phone numbers saved in the phone book. Scroll to the desired name or phone number, and press ")
            case "6":
                print("Copy:You can copy or move names and phone numbers from the phone to the SIM card (or vice versa) one by one or all at once. ")
            case "7":
                print("Assign tone: You can set the phone to play the desired ringing tone when you receive a call from a particular phone number. Scroll to the caller's name or phone number, press (Assign), and select the desired ringing tone.")
            case "8":
                print("Send b'card: You can send a name and phone number ('business card') as a text message to a compatible phone.")
            case "9":
                print("Options - Memory in use: You can select whether the names and phone numbers are saved in your phone or the SIM card. Note that when you change the SIM card, the SIM card option is automatically selected.")
            case "10":
                print("Options - Type of view: You can select the way the saved phone numbers and names are displayed.")
            case "11":
                print("Options - Memory status: Shows how many names and phone numbers can still be saved and are currently saved in the phone and the SIM card")
            case "12":
                print("Speed dials: You can set the desired number key (2 to 9) to work as a speed dialing key. Scroll to the desired key, press (Assign), and select a name or phone number.")
            case "13":
                print("========== Voice tags==========")
                print("You can dial a phone number by saying one or more words that you have attached to it as a 'voice tag' The voice tag can be, for example, a name, and you can record a voice tag to eight phone numbers in the phone book. You can also listen to, change, or erase the recorded voice tag.") 
                print("1 to record a voice tag")
                print("2 to make a call using a voice tag")
                print("3 to return to Phone book menu")
                voice_tag = input("Select an option: ")
                match voice_tag:
                    case "1":
                        print("Insert Sim Card\n");
                 
                    case "2":
                        print("Insert Sim Card\n");
                 
                    case "3" :
                        print("Returning to Phone Book Menu....");
                        phone_book();
                        return
                    case _: 
                        print("Invalid Entry...Try Again\n");
                        return
                 
            case "14":
                print("Returning to main menu...")
                
                return
            case _:
                print("Invalid Entry...Try Again")
                phone_book()
                return
                
       

        
def message():
    while True:
        print("Messages (Menu 2)")
        print("In this menu, you can manage the names and phone numbers in the phone and the SIM card.")
        print("1. Writing and Sending a text Message (Write messages)")
        print("2. Reading a text message (Inbox - Menu 2-2)")
        print("3. Picture messages(Menu 2-4)")
        print("4. Templates (Menu 2-5)")
        print("6. Message settings (Menu 2-7)")
        print("7. Info Service (Menu 2-8)")
        print("8. Voice mailbox number (Menu 2-9)")
        print("9. Service Command editor (Menu 2-10)")
        print("9. Smileys(Menu 2-6)")
        print("10. Back to Main Menu...")
        message = input("Select an option: ")
        match message:
            case "1":
                print(" ========== Writing and sending a test message  ==========")
                print("You can write and send multi-part text messages of almost up to three ordinary text messages in length (network service). Invoicing is based upon how many ordinary messages are needed for any multi-part message.")                               
                print("1 to write a message")
                print("2 to send a message")
                print("3 for Outbox")
                print("4 to return to Message menu")
                writing_message = input("Select an option: ")
                match writing_message:
                    case "1":
                        print("Insert Sim Card.")
                    case "2":
                        print("Insert Sim Card.")
                    case "3":
                        print("Insert Sim Card.")
                    case "3":
                        print("Returning to Message Menu....")
                        message()
                        return
                    case _:
                        print("Invalid Entry...Try Again")
                        return
                
            case "2":
                while True:
                    print("========== Reading a text message ==========")
                    print("You can write and send multi-part text messages of almost up to three ordinary text messages in length (network service). Invoicing is based upon how many ordinary messages are needed for any multi-part message.")                               
                    print("1 to read a message")
                    print("2 to move to next section of messages")
                    print("3 to return to Message menu")
                    reading_message = input("Select an option: ")
                    match reading_message:
                        case "1":
                            print("No message to read")
                        case "2":
                            print("No message to read")
                        case "3":
                            print("Returning to Message Menu....")
                            message()
                            return
                        case _:
                            print("Invalid Entry...Try Again")
                            return
                
            case "3":
                while True:
                    print("========== Picture messages ==========")
                    print("->You can send and receive text messages that contain pictures (network service). Note that Each picture message is made up of several text messages. Therefore, sending one picture message may cost more than one text message.")
                    print("->Since picture messages are saved in the phone, you cannot view them if you use the SIM card with another phone.")
                    print("1 to view received picture message")
                    print("2 to send picture message")
                    print(" 3 to return to Message menu")
                picture_method = input("Select an option: ")
                match picture_method:
                    case "1":
                        print("No picture to view")
                    case "2":
                        print("No picture to send")
                    case "3":
                        print("Returning to Message Menu....")
                        message()
                        return
                    case _:
                        print("Invalid Entry...Try Again")
                        return
                
            case "4":
                while True:
                    print(" ========== Template ==========")
                    print("You can view, edit or erase the template that can be used to write a message")
                    print("1 to go back to Message Menu")
               
                template = input("Select an option: ")
                match template:
                   
                    case "3":
                        print("Returning to Message Menu....")
                        message()
                        return
                    case _:
                        print("Invalid Entry...Try Again")
                        return
            case "5":
                 while True:
                    print("========== Message settings ==========")
                    print("This phone offers two kinds of message sets:")
                    print(" 1 for set 1")
                    print("2 for Common")
                    print("3 to return to Message menu")
                    message_setting = input("Select an option: ")
                    match message_setting:
                        case "1":
                            while True:
                                print("========== Set One ==========")
                                print("A set is a collection of settings needed for sending text and picture messages:")
                                print(" 1 for message centre number")
                                print("2 to send message as")
                                print("3 to verify message")
                                print("4 to return to Message menu")
                                set_one = input("Select an option: ")
                                match set_one:
                                    case "1":
                                        print("No Sim card inserted")
                                    case "2":
                                        print("No Sim card inserted")
                                    case "3":
                                        print("No Sim card inserted")
                        
                                    case "4":
                                        print("Returning to Message Menu....")
                                        message()
                                        return
                                    case _:
                                        print("Invalid Entry...Try Again")
                                        return
                        case "2":
                            while True:
                                print("========== Common ==========")
                                print("The settings in this submenu apply to all text that you send, irrespective of the chosen set:")
                                print("1 for Delivery report")
                                print("2 to reply via same centre")
                                print("3 for character support")
                                print("4 to return to Message menu")
                                common = input("Select an option: ")
                                match  common:
                                    case "1":
                                        print("No Sim card inserted")
                                    case "2":
                                        print("No Sim card inserted")
                                    case "3":
                                        print("No Sim card inserted")
                        
                                    case "4":
                                        print("Returning to Message Menu....")
                                        message()
                                        return
                                    case _:
                                        print("Invalid Entry...Try Again")
                                        return
                        case "3":
                            print("Returning to Message Menu....")
                            message()
                            return
                        case _:
                            print("Invalid Entry...Try Again")
                            return
            case "6":
                while True:
                    print(" ========== Info service ==========")
                    print("With this network service, you can receive messages on various topics from networks. For more detail contact service provider.")
                    print("1 to go back to Message menu")
                    info_service = input("Select an option: ")
                    match info_service:
                        case "1":
                            print("Returning to Message Menu....")
                            message()
                            return
                        case _:
                            print("Invalid Entry...Try Again")
                            return
                        
                    
            case "7":
                while True:
                    print("========== Voice mailbox number ==========")
                    print("You can save the phone number of your voice mailbox(Network service).")
                    print("1 to go back to Message menu")
                    voice_mailbox = input("Select an option: ")
                    match voice_mailbox:
                        case "1":
                            print("Returning to Message Menu....")
                            message()
                            return
                        case _:
                            print("Invalid Entry...Try Again")
                            return
                
            case "8":
                while True:
                    print("  ========== Service command editor ==========")
                    print(" You can send services request to your service provider.")
                    print("1 to go back to Message menu")
                    service_command = input("Select an option: ")
                    match service_command:
                        case "1":
                            print("Returning to Message Menu....")
                            message()
                            return
                        case _:
                            print("Invalid Entry...Try Again")
                            return
            
            case "9":
                while True:
                    print("  ========== Smileys ==========")
                    print(" You can create smiley charaters that you can use when writing or replying to a message.")
                    print("1 to go back to Message menu")
                    smiley = input("Select an option: ")
                    match smiley:
                        case "1":
                            print("Returning to Message Menu....")
                            message()
                            return
                        case _:
                            print("Invalid Entry...Try Again")
                            return
                
            case "10":
                print("Returning to main menu...")
                
                return
            case _ :
                print("Invalid Entry...Try Again")
                message()
                return
           
   
def chat():
    while True:
        print("Chat (Menu 3)")
        print("You can have a conversation with another person using text messages.")
        print("1 to Chat")
        print("2 to Enter Nickname")
        print("3 to Write a message")
        print("4 to Reply a message")
        print("5 to Return to Main Menu...")
       
        chat = input("Select an option: ")
        match chat:
            case "1": 
                print("Insert sim card")
            case "2":
                print("Insert sim card") 
            case "3":
                print("Insert sim card")
            case "4":
                print("Insert sim card")
            case "5":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                chat()
                return
                
def call_register():
    while True:
        print("Register (Menu 4)")
        print("In this menu, you can view the phone numbers registered by the phone and the approximate length and cost of your calls. You can also view and adjust the settings of a prepaid SIM card.")
        print("1. Missed calls")
        print("2. Received calls")
        print("3. Dialed numbers")
        print("4. Erase recent  call lists")
        print("5. Show call duration")
        print("6. Show call cost")
        print("7. Call cost settings")
        print("8. Prepaid credit")
        print("9. Back to Main Menu...")
        call_register = input("Select an option: ")
        match call_register:
             case "1":
               while True:
                print("========== Call register ==========")
                print("IN this function you can view the phone numbers registered by the phone and the approximate lenght cost of your calls.")                               
                print("1 for Missed calls")
                print("2 for Received calls")
                print("3 for Dialed numbers")
                print("4 for Erase recent call lists")
                print("5 for Show call lists")
                print("6 for Show call costs")
                print("7 for Call cost settings")
                print("8 for Prepaid Credit")
                print("9 for return to main menu")
                call_register = input("Select an option: ")
                match call_register:
                    case "1":
                        print("No missed calls")
                    case "2":
                        print("No received calls")
                    case "3":
                        print("No dialled numbers")
                    case "4":
                        print("No list to erase")
                    case "5":
                        print("No list to show")
                    case "6":
                        print("No cost to show")
                    case "7":
                        print("No limit set")
                    case "8":
                        while True:
                            print("========== Call register ==========")
                            print("IN this function you can view the phone numbers registered by the phone and the approximate lenght cost of your calls.")                               
                            print("1 for credit info display")
                            print("2 for cretid available")
                            print("3 for last event cost")
                            print("4 for recharge staus")
                            print("5 to retun to chat menu")
                            
    
                            prepaid_credit = input("Select an option: ")
                            match prepaid_credit:
                                case "1":
                                    print("No available credit")
                                case "2":
                                    print("No available credit")
                                case "3":
                                    print("No available credit")
                                case "4":
                                    print("No available credit")
                                case "5":
                                    print("Returning to Call Register Menu....")
                                    call_register()
                                    return
                                case _ :
                                    print("Invalid Entry...Try Again")
                                    return
                    case "9":
                        print("Returning to Message Menu....")
                        message()
                        return
                    case _:
                        print("Invalid Entry...Try Again")
                        call_register()
                        return
def tone():
    while True:
        print("Tones (Menu 5)")
        print("In this menu, you can change the settings of the currently selected profile.")
        print("1. Ringing Tone")
        print("2. Ringing volume")
        print("3. Incoming call alert")
        print("4. Message alert tone")
        print("5. Keypad tones")
        print("6. Warning tones")
        print("7. Vibrating alert")
        print("8. Screen Saver")
        print("9. Back to Main Menu...")
        tone = input("Select an option: ")
        match tone:
            case "1":
               print("Nokia default")
            case "2":
                print("Nokia default")
            case "3":
                print("Nokia default")
            case "4":
                print("Nokia default")
            case "5":
                print("Nokia default")
            case "6":
                print("Zig-Zag")
            case "7":
                print("Nokia default")
            case "8":
                print("Nokia default")
            case "9":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                tone()
                return
def setting():
    while True:
        print("Settings (Menu 6)")
        print("In this menu, you can adjust various settings of your phone. You can also reset some menu settings to their default values.")
        #print("1. Call settings")
        #print("2. Phone settings")
        #print("3. Security settings")
        #print("4. Restore factory settings")
        print("5. Back to Main Menu...")
       
        setting = input("Select an option: ")
        match setting:
            #case "1":
               
            #case "2":
                
            #case "3":
                
            #case "4":
            case "5":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                setting()
                return
        
def call_divert():
    while True:
        print("Call Divert (Menu 7)")
        print("You can direct your incoming calls to your voice mailbox or some other phones.")
        #print("1. ")
        #print("2. ")
        #print("3. ")
        #print("4. Back to Main Menu...")
       
        call_divert = input("Select an option: ")
        match call_divert:
            #case "1":
               
            #case "2":
                
            #case "3":
            
            case "4":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                call_divert()
                return
def music():
    while True:
        print("Music (Menu 8)")
        print("You can listen to music or the FM radio with your phone. You can also record music from the radio or an external music source. You can record or transfer music files of up to 2 hours of hear CD-quality music to the approximately 64 MB of free memory in your phone \nNote: Your phone must be switched on to use this function. Do not switch the phone on when wireless phone use is prohibited or when it may cause interference or danger.")
        #print("1. Music player (Menu 8-1)")
        #print("2. Radio (Menu 8-2)")
        #print("3. Recorder(Menu 8-3)")
        #print("4. Track list (Menu 8-4)")
        print("5. Back to Main Menu...")
       
        music = input("Select an option: ")
        match music:
            #case "1":
               
           # case "2":
                
            #case "3":
                
            #case "4":
            case "5":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                music()
                return
def game():
    while True:
        print("Game (Menu 9)")
        print("The phone offers you the following games to play: Snake II, Space Impact, Bantumi Pairs II, and Bumper. \nYou can use the keys on either side of the screen for playing. The key pattern is duplicated so that it is identical on both sides of the keyboard. This way you can select whether you want to play on one side only or on both sides with allows more room for both hands. \nNote: Your phone r must be switched on to use this function. Do not switch the phone on when wireless phone use is prohibited or when it may cause interference or danger.")
        print("1. Adjusting settings common to all games ")
        print("2. Starting a game and adjusting game-specific settings ")
        print("3. Making a connection to the WAP service of Club Nokia")
        print("4. Game keys ")
        print("5. Back to Main Menu...")
       
        game = input("Select an option: ")
        match game:
            #case "1":
               
            #case "2":
                
           # case "3":
                
           # case "4":
            case "5":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                game()
                return
def calulator():
    while True:
        print("Calculator (Menu 10)")
        print("The phone is provided with a calculator which can also be used for rough currency conversion.")
        print("1. Making a calculation")
        print("2. Making a currency conversion")
        print("3. Currency conversion on standby mode")
        print("4.  Back to Main Menu...")
       
        calculator = input("Select an option: ")
        match calculator:
            #case "1":
               
            #case "2":
                
           # case "3":
                
            case "4":
                print("Returning to main menu...")
                return
               
            case _ :
                print("Invalid Entry...Try Again")
                calculator()
                return
def reminder():
    while True:
        print("Reminder (Menu 11)")
        print("With this memory aid, you can save short text notes with an alarm. The alarm goes off when the set date and time is reached .")
        print("1. Add new")
        print("2. View all")
        print("3. Back to Main Menu...")
       
        reminder = input("Select an option: ")
        match reminder:
            #case "1":
               
            #case "2":
                
            case "3":
                print("Returning to main menu...")
                return   
            case _ :
                print("Invalid Entry...Try Again")
                reminder()
                return
def clock():
    while True:
        print("Clock (Menu 12)")
        print("In this menu, you can adjust and use the time-related features of your phone.")
        print("1. Clock Settings")
        print("2. Date setting")
        print("3. Stopwatch")
        print("4. Countdown timer")
        print("5. Auto update of date and time")
        print("6. Back to Main Menu...")
       
        clock = input("Select an option: ")
        match clock:
            #case "1":
               
            #case "2":
                
            #case "3":
                
            #case "4":
            #case "5":
            case "6":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                clock()
                return
def profile():
    while True:
        print("Profile (Menu 13)")
        print("In this menu, you can edit, manage, and create the setting groups ('profiles') that control all the phone tones in different environments. One profile is always in use. \nYou can easily change the settings of the currently selected profile also in the Tones menu (Main Menu 5).")
        print("1. Activating a profile and changing its settings")
        print("2. Back to Main Menu...")
       
        profile = input("Select an option: ")
        match clock:
            #case "1":
            case "2":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                profile()
                return
def service():
    while True:
        print("WAP services (Services Menu 14)")
        print("In this menu, you can access various WAP (Wireless Application Protocol) services such as banking, online games, and entertainment. These services are specifically designed for mobile phones, and they are maintained by WAP service providers.")
        #print("1. Basic steps for accessing and using WAP service")
        #print("2. Setting up the phone for a WAP service")
        #print("3. Making a connection to a WAP service")
        #print("4. Browsing the pages of a WAP service")
        #print("5. Ending a WAP connection")
        #print("6. Adjusting the appearance setting of WAP pages")
        #print("7. Saving and managing bookmarks")
        #print("8. Emptying the cache memory ")
        #print("9. Having a WAP connection and a voice call in progress at the same time (when the bearer is USSD)")
        #print("10. Security Certification")
        print("11. Back to Main Menu...")
        service = input("Select an option: ")
        match service:
           # case "1":
               
            #case "2":
                
            #case "3":
                
            #case "4":
            #case "5":
            #case "6":
            #case "7":
            #case "8":
            #case "9":
            #case "10":
            case "11":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                service()
                return
def sim_service():
    while True:
        print("Sim Services (Menu 15)")
        print("This menu is shown only if your sim card provides additional services. The name and content of this menu depends on the service available.")
        print("1. Activating a profile and changing its settings")
        print("2. Back to Main Menu...")
       
        clock = input("Select an option: ")
        match clock:
            case "1":
                print("Returning to main menu...")
                return
            case _ :
                print("Invalid Entry...Try Again")
                clock()
                return



while True:
    print("                 NOKIA 5510 USER MANUAL                  ")
    print("MAIN MENU OF FUNCTIONS")
    print("1. Phone Book")
    print("2. Message")
    print("3. Chat")
    print("4. Call register")
    print("5. Tones")
    print("6. Settings")
    print("7. Call Divert")
    print("8. Music")
    print("9. Games")
    print("10. Calculator")
    print("11. Reminder")
    print("12. Clock")
    print("13. Profile")
    print("14. Service")
    print("15. Sim Services")
    print("16. Exit")
    
    choice = input("Enter an option: ")
    match choice:
        case "1":
            phone_book()
        case "2":
            message()
        case "3":
            chat()
        case "4":
            call_register()
        case "5":
            tone()
        case "6":
            setting()
        case "7":
            call_divert()
        case "8":
            music()
        case "9":
            game()
        case "10":
            calculator()
        case "11":
            reminder()
        case "12":
            clock()
        case "13":
            profile()    
        case "14":
            service()
        case "15":
            sim_service()
        case "16":
            print("Thank you for choosing Nokia!!!")
            break
        case _ :
            print("Invalid Input")
