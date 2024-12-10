class Bank_account:    
    def __init__(self, owner = str, balance: int = 0):
        self.__balance = balance
        self.__owner = owner

    def get_balance(self):
        return self.__balance
    def get_owner(self):
        return self.__owner
    def set_owner(self, owner: str):
        self.__owner = owner
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount: float):
        if 0 < amount < self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Funds")