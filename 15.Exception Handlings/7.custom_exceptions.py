class InsufficientBalanceError(Exception):
    pass

def withdraw_money(balance,amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient Balance")
    print(f"Balance = {balance - amount}")

try:
    withdraw_money(2000,3000)
except Exception as e:
    print(type(e).__name__)
    print(e)
