
def make_withdrawal(balance):
    def inner(withdraw):
        nonlocal balance
        if (withdraw > balance):
            raise ValueError("Balance less than withdraw amount.")
        else:
            balance = balance - withdraw
            print("Withdraw", withdraw,"from account.")
            print("Balance now is", balance)
            return balance
    return inner


init_balance = 100
withdrawal_amount = 10
new_withdrawal_amount = 20

wd = make_withdrawal(init_balance)
wd(withdrawal_amount)
wd(new_withdrawal_amount)