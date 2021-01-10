class Bill():
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Negative value is not allowed")
        if type(amount) != int:
            raise TypeError("Amount has to be an int value")

        self._amount = amount

    def __eq__(self, other):
        return other and other._amount == self._amount

    def __str__(self):
        return "A " + str(self._amount) + "$ bill"

    def __int__(self):
        return self._amount

    def __lt__(self, other):
        return (self._amount < other._amount)
    
    def __repr__(self):
        return "Bill($" + str(self._amount) + ")"

    def __hash__(self):
        return hash(self._amount)


class BatchBill():
    def __init__(self, bills):
        self._bills = bills

    def __len__(self):
        return len(self._bills)

    def __getitem__(self, index):
        return self._bills[index]

    def __repr__(self):
        msg = ""
        for bill in self._bills:
            msg += "Bill($" + str(bill._amount) + ")"
        return msg

    def __int__(self):
        return self.total()

    def total(self):
        sum = 0
        for bill in self._bills:
            sum += int(bill)
        return sum


class CashDesk():
    def __init__(self):
        self._bills = []

    def take_money(self, bills):
        if type(bills) is BatchBill:
            for x in bills:
                self._bills.append(x)
        else:
            self._bills.append(bills)

    def total(self):
        sum = 0
        for bill in self._bills:
            sum += int(bill)
        return sum

    def inspect(self):
        message = "We have a total of " + str(self.total()) + "$ in the desk\n"
        message += "We have the following count of bills, sorted in ascending order:\n"
        
        d = {}
        for x in self._bills:
            amount = x._amount
            if amount in d:
                d[amount] += 1
            else:
                d[amount] = 1
        
        for key in sorted(d):
            message += str(key) + "$ bills - " + str(d[key]) + "\n"

        return message[:-1]
