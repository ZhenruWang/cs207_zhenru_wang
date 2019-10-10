print("The following code does not work because the balance cannot be updated " \
      "directly in the inner function. The inner function would have a balance variable in " \
      "a new scope that is different than the balance as the parameter.")

def make_withdrawal(balance):
    def inner(withdraw):
        balance = balance-withdraw
        if (withdraw > balance):
            raise ValueError("Balance less than withdraw amount.")
        else:
            return balance
    return inner


init_balance = 100
withdrawal_amount = 10
new_withdrawal_amount = 20

wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)