class BankAccount:
    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError("Balance can't be negative")
        if currency is None or len(currency) < 1:
            raise ValueError("Currency can't be empty")
        self._name = name
        self._balance = balance
        self._currency = currency
        self._history = ["Account was created"]

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount can't be negative")
        self._balance += amount
        self._history.append("Deposited {}{}".format(amount, self._currency))

    def balance(self):
        self._history.append("Balance check -> {}{}".format(self._balance, self._currency))
        return self._balance


    def withdraw(self, amount):
        if self._balance > amount:
            self._balance -= amount
            return True
        return False

    def __str__(self):
        return "Bank account for {} with balance {.2}{}".format(self._name, self._balance, self._currency)

    def __int__(self):
        self._history.append("__int__ check -> {}{}".format(self._balance, self._currency))
        return self._balance
        
    def history(self):
        return self._history

    def transfer_to(self, other_account, amount):
        if self._currency is not other_account._currency:
            raise TypeError("Transfer are allowed only between accounts with the same currency")
        if amount < 0:
            raise ValueError("Amount is negative")
        if self._balance < amount:
            raise Exception("Funds not sufficient")
        other_account._balance += amount
        self._balance -= amount
