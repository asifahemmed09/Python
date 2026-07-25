class Bank:
    def __init__(self,name: str, balance: int):
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid Amount")
        else:
            self.__balance += amount
    def get_balance(self):
        return self.__balance

b1 = Bank("John", 10000)
print(b1.get_balance())

b1.deposit(5000)
print(b1.get_balance())

# name mangling
print(b1._Bank__balance)

