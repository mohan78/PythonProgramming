"""
    Write a class that will create a banking application object that has the following
    attributes:
    full_name
    account_no
    starting_balance

    And it should have the following methods:
    .show_balance: Should return the balance the user has
    .credit(amount): Should add the given amount to the balance
    .debit(amount): Should reduce the given amount from the balance
"""

class Banker:
    
    def __init__(self, first_name, last_name, account_no, starting_bal) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.account_no = account_no
        self.balance = starting_bal

    def show_balance(self):
        return self.balance

    def credit(self, amount):
        if amount <= 0:
            return "Amount should be number greater than zero"
        self.balance += amount
        return f"Balance for account number {self.account_no} after crediting {amount} is {self.balance}"

    def debit(self, amount):
        if amount <= 0:
            return "Amount should be greater than zero"
        if self.balance < amount:
            return "Not enough funds in your account"
        self.balance -= amount
        return f"Balance for account number {self.account_no} after debiting {amount} is {self.balance}"
    
    @classmethod
    def create_user(cls, full_name, account_no, starting_bal):
        names_after_split = full_name.split(' ')
        first_name = names_after_split[0]
        last_name = names_after_split[len(names_after_split)-1]
        return cls(first_name, last_name, account_no, starting_bal)
    

mohan = Banker('Mohan', 'Peddapuli', 1, 100)
print(mohan.credit(1000))
print(mohan.show_balance())

vasanthi = Banker.create_user('Vasanthi Peddapuli', 2, 1000)
print(vasanthi.debit(300))
print(vasanthi.show_balance())
