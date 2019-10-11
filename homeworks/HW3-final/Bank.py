from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2
    
class BankAccount:
    
    
    def __init__(self, owner, accountType):
        self.owner = owner
        self.accountType = accountType
        self.balance = 0
    def __str__(self):
        res = "This account belongs to " + self.owner
        res += "\nThis account is of type " + self.accountType.name
        res += "\nThe balance of the account is" + str(self.balance)
        return res
    
    def __len__(self):
        return self.balance
    
    #You should not be able to withdraw more money than the balance of the account.
    #You should not be able to withdraw or deposit a negative amount.
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise ValueError("The amount exceeds account balance.")
        else:
            if amount < 0 :
                raise ValueError("The withdraw amount cannot be negative.")
            else:
                self.balance = self.balance - amount
        return 0
    
    def deposit(self, amount):
        if amount < 0 :
            raise ValueError("The deposit amount cannot be negative.")
        else:
            self.balance = self.balance + amount
        return 0
        
    

class BankUser:
    
    def __init__(self, owner):
        self.owner = owner
        self.account = []
        self.have_saving = False
        self.have_checking = False
        
    def __str__(self):
        return "informative summary"
    
    def addAccount(self, accountType):
        #Only one savings and checking account per user. 
        #Raise an appropriate error otherwise.
        #have_saving = False
        #have_checking = False
        for a in self.account :
            if a.accountType == AccountType.SAVINGS:
                self.have_saving = True
            elif a.accountType == AccountType.CHECKING:
                self.have_checking = True
        # Checked if s/c account alreay exists
        if self.have_saving and accountType == AccountType.SAVINGS:
            raise ValueError("Already have a savings account")
        elif self.have_checking and accountType == AccountType.CHECKING:
            raise ValueError("Already have a checking account")
        else:
            newacc = BankAccount(self.owner,accountType)
            self.account.append(newacc)
            #print(newacc)
        return 0
    
    def getBalance(self, accountType):
        for a in self.account :
            if a.accountType == accountType:
                accountname = accountType.name
                print("The balance for ",accountname,"is ",a.balance)
                return a.balance
        return 0
    
    
    def deposit(self, accountType, amount):
        #print("in deposit")
        for a in self.account :
            #print("in deposit loop")
            if a.accountType == accountType:
                a.deposit(amount)
                return None
        print("No account found. Please try again")
        
    
    def withdraw(self, accountType, amount):
        for a in self.account :
            if a.accountType == accountType:
                a.withdraw(amount)
        return 0
        
        

#ATMSession(bankUser)
def ATMSession(bankUser):
    def Interface():
        loop = True
        while loop:
            txt = input("Enter Option:\n" + "1)Exit\n"+ "2)Create Account\n"+ "3)Check Balance\n"+ "4)Deposit\n"+ "5)Withdraw\n")
            
            if txt == "1":
                break
            elif (txt == "4" or txt == "5"):
                #get account type
                txt_type = input("Enter Option:\n" + "1)Checking\n"+ "2)Savings\n")
                acc_type = AccountType(int(txt_type))
                
                #get amount input
                txt_amount = input("Enter Integer Amount, Cannot Be Negative:\n")
                # make amount is integer
                try:
                    amount = int(txt_amount)
                except ValueError:
                    print("Please enter an integer amount")
                # make sure amount is positive integer
                if amount < 0:
                    #raise ValueError("Amount cannot be negative")
                    print("Amount cannot be negative")
                    pass
                else:
                    if txt == "4":
                        #print("In interface deposit")
                        try:
                            bankUser.deposit(acc_type,amount)
                            print("Deposit successful")
                        except Exception as e:
                            print(e)
                    else:
                        try:
                            bankUser.withdraw(acc_type,amount)
                            print("Withdraw successful")
                        except Exception as e:
                            print(e)    
                        
            elif (txt == "2"):
                #create account
                #ask for account type
                txt_new = input("Enter Option:\n" + "1)Savings\n"+ "2)Checking\n")
                print("Is this what you input",txt_new)
                acc_type = AccountType(int(txt_new))
                try:
                    bankUser.addAccount(acc_type)
                    print("Account created successful.")
                except Exception as e:
                    print(e)
                    
            elif (txt == "3"):
                # Check balance
                #ask for account type
                txt_new = input("Enter Option:\n" + "1)Savings\n"+ "2)Checking\n")
                acc_type = AccountType(int(txt_new))
                balance = bankUser.getBalance(acc_type)
                print("Your account balance is", balance)
            else:
                print("Invalid input. Please try again.")
            # end while
        return None
    return Interface



#bankUser = BankUser("Emma")
#Interface(bankUser)