savings_balance = 500000
current_balance = 10000000
def linked_banks():
    while True:
        print("                 Linked Banks                    ")
        print("1. UBA")
        print("2. Zenith Bank")
        print("3. Modius Bank")
        print("4. Stanbic")
        print("5. Return to Withdraw Menu")
        bank = input("Choose a Linked Bank: ")
        match bank:
            case "1":
                print("Selecetion received....Debiting UBA Account")
            case "2":
                print("Selection received....Debiting Zenith Account")
            case "3":
                print("Selection received....Debiting Modius Account")
            case "4":
                print("Selection received....Debiting Stanbic Account")
            case "5":
                withdraw_amount()
                return
            case _ :
                print("Invalid Account")
                break
        
def checker_balance():
    while True:
        print("======ACCOUNT BALANCE MENU======")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. Return to Main Menu...")
        account = input("Select account: ")
        match account:
            case "1":
                print("Savings balance:", savings_balance)
                
            case "2":
                print("Current balance:", current_balance)
            case "3" :
                print("Return to Main Menu")
                return    
            case _ :
                print("Invalid Input")
                
            
def withdraw_amount():
    while True:
        print("========Withdraw Menu=========")
        print("1. Savings Account")
        print("2. Current Account")
        print("3. From Linked Account")
        print("4. Return to Main Menu...")
        
        account = input("Select account to withdraw: ")
       
        match account:
            case "1" :
                print("Saving account selected")
            case "2" :
                print("Current account selected")
            case "3" :
                linked_banks()
                
            case "4" :
                print("Returning to Main Menu")
                return
            case _ :
                print("Invalid Entry.")
                return
                withdraw_amount()
                
        savings_balance = 500000
        current_balance = 10000000        
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0 and account == "_" :
            print("Invalid Amount")
        elif amount <= savings_balance  and account == "1":
            savings_balance -= amount
            print("", amount, "Successfully withdrawn from savings account, you have", savings_balance, "remaining.")
        elif amount <=  current_balance and account == "2":
            current_balance -= amount
            print("", amount, "Successfully withdrawn from current account", current_balance)
        else:
            print("Insufficient Balance")
       
        


    
while True:    
    print("===========Main Menu===========")
    print("1. Check balance")
    print("2. Withdraw amount")
    print("3. Transfer Amount")
    print("4. Exit process")

    choice = input("Select an option: ")
    match choice:
        case "1":
            checker_balance()
        case "2" :
            withdraw_amount()
        case "3" :
            transfer_amount()
        case "4":
            print("Thank you for banking with us")
            break
        case _ :
            print("Invalid Input")
       
     
     


    
    
