print("The following code does not work because the balance was only assigned " \
      "once in the decorator function, it did not get updated after the withdraw. ")
def make_withdrawal(balance):
    def inner(withdraw):
        if (withdraw > balance):
            raise ValueError("Balance less than withdraw amount.")
        else:
            return balance-withdraw
    return inner


init_balance = 100
withdrawal_amount = 10
new_withdrawal_amount = 20

wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)