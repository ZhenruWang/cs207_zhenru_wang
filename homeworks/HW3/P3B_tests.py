from Bank import BankUser
from Bank import AccountType

def test_over_withdrawal(): #this test function should throw an
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS, 10)
    try:
        user.withdraw(AccountType.SAVINGS, 1000) #this should throw an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption
print("Testing when amount withdraw exceeds balance:")   
test_over_withdrawal()
    
def test_create_same_account(): #this test function should throw an
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    try:
        user.addAccount(AccountType.SAVINGS) #this should throw an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption   
        
print("Testing creating an account when savings account already exists:")       
test_create_same_account()

def test_create_same_checking_account(): #this test function should throw an
    user = BankUser("Joe")
    user.addAccount(AccountType.CHECKING)
    try:
        user.addAccount(AccountType.CHECKING) #this should throw an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption   
        
print("Testing creating an account when checkingaccount already exists:")       
test_create_same_checking_account()

def test_deposit_wrong_account(): #this test function should throw an
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    try:
        user.deposit(AccountType.CHECKING,100) #this should throw an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption   

print("Testing depositing to an account that does not exist:")       
test_deposit_wrong_account()

def test_deposit_wrong_amount(): #this test function should throw an
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    
    try:
        user.deposit(AccountType.SAVINGS,-100) #this should throw an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption 
    
print("Testing deposting the wrong amount:")
test_deposit_wrong_amount()

def test_withdraw_wrong_amount():
    #this test function should throw an
    user = BankUser("Joe")
    user.addAccount(AccountType.SAVINGS)
    user.deposit(AccountType.SAVINGS,100)
    try:
        user.withdraw(AccountType.SAVINGS,-100) #this should throw an Exception or Error
    except Exception as e:
        print(e) #print the message for the Exeption 

print("Testing withdraw the wrong amount:")
test_withdraw_wrong_amount()
