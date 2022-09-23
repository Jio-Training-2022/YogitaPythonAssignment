bankacct = [
    {   "Account":1,
        "Name":'X',
        "Deposit":1000,
        "Withdrawal":500
    }
]

def add_new_acct(acct):
    i=0
    while i<len(bankacct):
        if acct==bankacct[i][0]:
            print('Enter unique Bank account number.')
            break
            
    else:
        print("Your acct is " + acct)
        name=str(input('Enter account name.'))
        deposit=float(input('Enter your deposit amount.'))
        withdrawal=float(input('Enter your withdrawal amount.'))
        balance=deposit-withdrawal
        print(balance)


    new_acct=int(input('Enter new account number.'))
    add_new_acct(new_acct)





# def add_new_acct(acct):
#     for i in range(len(bankacct)):
#         for j in bankacct[i][0]:
#             if acct==j:
#                 print('This number exists. Enter new unique account number.')
#                 acct=int(input('Enter account number'))
#                 new_acct(acct)
#             else:
#                 print("Your acct is " + acct)
#                 name=str(input('Enter account name.'))
#                 deposit=float(input('Enter your deposit amount.'))
#                 withdrawal=float(input('Enter your withdrawal amount.'))
#                 balance=deposit-withdrawal
#                 print(balance)


acct=int(input('Enter account number'))
add_new_acct(acct)



    # for i in range(len(bankacct)):
    #     if acct==bankacct[i][0]:
    #         print('This account number exists already. Enter unique number to add new account.')
    #         sdd_new_acct()
    #     else:





