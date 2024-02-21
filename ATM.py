# import random
# while True:
#     print("1.Check Balance")
#     print("2. Deposit Funds")
#     print("3. Withdraw Funds")
#     print("4. Exit")
#     choice=int(input("Enter Your Choice: "))
#     balance = random.randint(2000,10000)
#     if choice ==1:
#         print("Your Balance is ",balance)
#     elif choice ==2:
#         deposit=int(input("Enter The Amount To Deposit:"))
#         u_balance =balance +deposit
#         print("Old Balance ",balance)
#         print("Your Updated Balance ",u_balance)

#     elif choice ==3:
#         withdraw = int(input("Enter The Amount To withdraw:"))
#         u_balance = balance - withdraw
#         print("Old Balance ", balance)
#         print("Your Updated Balance ", u_balance)
#     elif choice ==4:
#         print("Thank U For Using Our Services ")
#         break
 import random
while True:
    print("1.Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")
    choice=int(input("Enter Your Choice:"))
    balance = random.randint(2000,10000)
    if choice == 1:
        print("Your Balance is ₹", balance)
    elif choice == 2:
        deposit = int(input("Enter The Amount To Deposit:"))
        u_balance = balance + deposit
        print("Old Balance ₹", balance)
        print("Your Updated Balance ₹", u_balance)
    elif choice == 3:
        if balance <2000:
            print("Sorry Plz. maintain your Minimum Balance :( ")
        else:
            withdraw = int(input("Enter The Amount To withdraw:"))
            u_balance = balance - withdraw
            print("Old Balance ₹", balance)
            print("Your Updated Balance ₹", u_balance)
    elif choice == 4:

        print("Thank U For Using Our Services :)")
        break                                                                                                                                                                                                                                                                                                                                                               