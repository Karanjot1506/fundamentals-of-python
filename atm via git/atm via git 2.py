def withdraw(transaction,balance,amount):
    print(type(transaction))
    if balance <= 0:
        print("insuffecient balance:")
    elif balance < amount :
        print("enter amount less than balance")
    elif amount !=100 == 0 :
        print("enter amount multiple of 100")
    else:
        transaction.append({"amt":amount,"data":"11 th june,2020"})
        print("your current balance is ",balance-amount)
    return balance
