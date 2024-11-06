initial_balance = 0
active = True 
while active: 
    amount = int(input("\nEnter the amount of transaction : "))
    transaction_type =str(input("\nEnter 'D' for Deposit or 'W' for withdrawal : "))
    if(transaction_type=="D"):
        initial_balance -= amount
        print("\nYour Net balance is : " , initial_balance)
    elif (transaction_type=='W'):
        if(amount<=initial_balance):
            initial_balance -= amount 
            print("\nYour Net Balance is : " , initial_balance)
    elif (amount>initial_balance):
        print("\nBalance insufficient")
    else: 
        print("\nInvalid Input")
    
    command = input("\nDo you want to make another transaction, enter 'Y' for yes and 'N' for No : ")
    if(command=="N"): 
        active = False

