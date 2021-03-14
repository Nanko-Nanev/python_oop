class Account:
    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"{__class__.__name__}({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        res = self._transactions + other._transactions
        Account(f"{self.owner}&{other.owner}", res)
        return res

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        if Account.validate_transaction(self, amount):
            self.amount += amount
            self._transactions.append(amount)
            return f"New balance: {self.amount}"

    @property
    def balance(self):
        return sum(self._transactions) + self.amount

    def validate_transaction(self, amount_to_add):
        if self.amount + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        else:
            return True

    @property
    def transactions(self):
        return self._transactions

    @transactions.setter
    def transactions(self, value):
        self._transactions = value


acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)
